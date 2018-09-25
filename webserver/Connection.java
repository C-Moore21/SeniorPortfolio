/**
 * Where the webserver logic lives.
 * @author Camden Moore
 */

import java.net.*;
import java.io.*;
import java.util.*;
import java.text.*;

public class Connection implements Runnable {
public static final int BUFFER_SIZE = 256;
private Socket client;
private Configuration configuration;
BufferedReader in = null;
OutputStream out = null;

public Connection(Socket client, Configuration configuration) {
        this.client = client;
        this.configuration = configuration;
}

public void writeLog(String request, String status_code, File resource) throws IOException {
        File log = new File(configuration.getLogFile());
        //check if the log file exists if not create it
        if (!log.exists()) {
                log.createNewFile();
        }
        //the 'true' flag allows appending.
        FileWriter fileWriter = new FileWriter(log, true);
        PrintWriter printWriter = new PrintWriter(fileWriter);
        //building the logging string.
        String log_string = client.getLocalAddress().toString() + " " +
                            getTime() + " " +
                            request + " " +
                            status_code + " " +
                            resource.length() + "\n";
        printWriter.print(log_string);
        printWriter.close();
}


public static String getTime() {
        // used the following resources to get the current time.
        //https://beginnersbook.com/2013/05/current-date-time-in-java/
        //https://docs.oracle.com/javase/1.5.0/docs/api/java/text/SimpleDateFormat.html
        Calendar calendar = Calendar.getInstance();
        SimpleDateFormat dateFormat = new SimpleDateFormat("EEE, dd MMM yyyy HH:mm:ss z", Locale.US);
        dateFormat.setTimeZone(TimeZone.getTimeZone("GMT"));
        return dateFormat.format(calendar.getTime());
}

public String header(String statusCode, File resource) {
        byte[] bytes = new byte[BUFFER_SIZE];

        //Using a regular expression to get the content type.
        String type = resource.getName().split("\\.(?=[^\\.]+$)")[1];

        //Building the header
        String header = "HTTP/1.1 " + statusCode + "\r\n" +
                        "Date: " + getTime() + "\r\n" +
                        "Server: " + configuration.getServerName() + "\r\n" +
                        "Content-Type: " + type + "\r\n" +
                        "Content-Length: " + resource.length() + "\r\n" +
                        "Connection: close\r\n\r\n";
        return header;
}
public void run() {
        try {
                String request;
                String[] request_split;
                String return_doc = null;
                String formattedHeader = null;
                String status_code;
                byte[] buffer = new byte[BUFFER_SIZE];
                int numBytes;

                BufferedReader in =
                        new BufferedReader(new InputStreamReader(client.getInputStream()));
                OutputStream out =
                        new BufferedOutputStream(client.getOutputStream());

                request = in.readLine();
                request_split = request.split(" ");
                return_doc = request_split[1];

                //Checking to see if the requested resource is the home page.
                if (return_doc.equals("/") || return_doc.equals(" ")) {
                        return_doc = configuration.getDefaultDocument(); //get default document
                } else {
                        if(request_split[1].toLowerCase().contains(configuration.getDocumentRoot().toLowerCase())) {
                                return_doc = request_split[1];
                        }
                        else {
                                return_doc = configuration.getDocumentRoot() + request_split[1];
                        }
                        System.out.println(return_doc);
                }


                File requested_file = new File(return_doc);

                //Checking to see that the requested resource exists and it isn't a directory
                if (requested_file.exists() && !requested_file.isDirectory()) {
                        //Storing the status code in a variable to pass to log
                        //Sending data to header() function to generate header.
                        status_code = "200 OK";
                        formattedHeader = header(status_code, requested_file);

                } else {
                        //Storing the status code in a variable to pass to log
                        //Sending data to header() function to generate header.
                        status_code = "404 Not Found";
                        return_doc = configuration.get404();
                        requested_file = new File(return_doc);
                        formattedHeader = header(status_code, requested_file);
                }
                //Writing out the formatted header created from the header() function
                out.write(formattedHeader.getBytes());
                out.flush();

                InputStream file = new BufferedInputStream(new FileInputStream(return_doc));

                while ((numBytes = file.read(buffer)) != -1) {
                        out.write(buffer, 0, numBytes);
                }
                writeLog(request, status_code, requested_file);

                //Closing out all opened streams.
                out.flush();
                file.close();
                in.close();
                out.close();
                client.close();

        } catch (java.io.IOException ioe) {
                System.err.println(ioe);
        }

}



}
