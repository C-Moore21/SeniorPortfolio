/**
 * A web server based on the Multi threaded Echo Server.
 * @author - Camden Moore.
 */

import java.net.*;
import java.io.*;
import java.util.concurrent.*;

public class WebServer
{
//listening for connections on port 8080
public static final int DEFAULT_PORT = 8080;

// construct a thread pool for concurrency
private static final Executor exec = Executors.newCachedThreadPool();

public static void main(String[] args) throws IOException {
        ServerSocket sock = null;
        Configuration configuration = null;

        try {
                // establish the socket
                sock = new ServerSocket(DEFAULT_PORT);

                while (true) {
                        //Getting the conf location for the loading of the configuration.
                        String conf = args[0];
                        try{
                                configuration = new Configuration(conf);
                        }catch(ConfigurationException e) {
                                System.err.println(e);
                        }

                        Runnable task = new Connection(sock.accept(),configuration);
                        exec.execute(task);
                }
        }
        catch (IOException ioe) { }
        finally {
                if (sock != null)
                        sock.close();
        }
}
}
