package subtitle_editor;

import java.io.File;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class App {
    public static void main(String[] args) {
        String path = "";
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Enter the path of the file with subtitles:");
            while (true) {
                try {
                    path = scanner.nextLine();
                    if (!path.contains(".txt")) throw new Exception("The file must be in txt format.");
                } catch (Exception e) {
                    System.err.println("You have entered an invalid path. \nHere is an example: \"C:\\Users\\Owner\\Desktop\\subtitles.txt\". Try again.");
                    scanner.reset();
                    scanner.next();
                    continue;
                }
                break;
            }   if (path.contains("\"")) {
                path = path.replace("\"", "");
            }
        } catch (Exception e) {
            System.err.println("An error occurred while reading the path.");
            return;
        }

        File Obj = new File(path);
        try {
            Scanner aReader = new Scanner(Obj);
            List<String> text = new ArrayList<>();
            while (aReader.hasNextLine()) {
                String line = aReader.nextLine();

                String regex = "[^a-zäöüßA-ZÄÖÜ.,>?!()']";
                line = line.replaceAll("(\\d+),", "");
                line = line.replaceAll(regex, " ");
                line = line.replaceAll("\\s+", " ");
                line = line.replaceAll(">", "\n");
                text.add(line);
                System.out.println(line);

            }

            Path newFile = Paths.get(path.replace(".txt", "_new.txt"));
            Files.write(newFile, text, StandardCharsets.UTF_8);
            aReader.close();
        } catch (Exception e) {
            System.err.println("File not found");
            e.printStackTrace();
        }
    }
}
