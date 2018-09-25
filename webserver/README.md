A WebServer based on the EchoServerMT provided in the course.

To run:
-Navigate to your directory where you placed the WebServer.java and all associated files in the zip.
-Compile all the .java files.
-execute: $java WebServer [absolute path to your config.xml file]


Your config.xml file should look similar to this:
        <?xml version='1.0'?>

        <!-- WEB SERVER META DATA -->
        <webserver
            title="Webserver"
            date="March 24 2018"
            author="Camden Moore"
        >

        <!-- DEFAULT DOCUMENTS -->
        <!-- macOS style -->
        <context defaultDocument = "/Users/camdenm/school/compsci/networking/homework4/website/template/index.html"></context>

        <!-- DOCUMENT ROOT -->
        <!-- Unix style -->
        <context documentRoot = "/Users/camdenm/school/compsci/networking/homework4/website/"></context>

        <!-- LOG FILE -->
        <!-- macOS / Linux style -->
        <logfile log = "/Users/camdenm/school/compsci/networking/homework4/server/logs/log.txt"></logfile>

        <!-- 404 FILE -->
        <!-- macOS / Linux style -->
        <context fourohfour = "/Users/camdenm/school/compsci/networking/homework4/website/template/404.html"></context>

        </webserver>
