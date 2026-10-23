// Extract a tar archive with Apache Commons Compress's Expander, for corpus/matrix.py.
//
//     java -cp 'JARS/*' Extract.java ARCHIVE DEST
//
// with the jars of jars.txt in JARS. An error is printed on stderr, with status 1.
import java.nio.file.Path;
import org.apache.commons.compress.archivers.examples.Expander;

public class Extract {
    public static void main(String[] args) {
        try {
            new Expander().expand("tar", Path.of(args[0]), Path.of(args[1]));
        } catch (Exception e) {
            System.err.println(e);
            System.exit(1);
        }
    }
}
