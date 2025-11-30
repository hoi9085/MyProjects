package front;
import java.io.File;
import java.io.IOException;
import java.net.URL;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
/** Obtenir une musique ou un effet sonore,
 * et en gérer ses propriétés tel que le volume et leur état.
 */
public class Sound {
    // Clip permettant de manipuler un fichier audio
    Clip clip;
    // Liste des URL de tous les sons (disponible dans res/sound/)
    URL soundURL[] = new URL[4];
    /** Constructeur d'un son. */
    public Sound(){
        try {
            soundURL[0] = new File("front/res/sound/BeepBox-Song.wav").toURI().toURL();
            soundURL[1] = new File("res/sound/BeepBox-Song.wav").toURI().toURL(); // Réutiliser le même fichier pour l'index 1
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /** Instancie un fichier parmi la liste des sons existants.
     * @param i index de l'URL du son
     */
    public void setFile(int i) {
        try {
            AudioInputStream ais = AudioSystem.getAudioInputStream(soundURL[i]);
            clip = AudioSystem.getClip();
            clip.open(ais);
        } catch (Exception e) {
        }
    }
    /** Démarre la lecture du fichier audio. */
    public void play() {
    if (clip != null) {  // Vérifier que le clip n'est pas null avant de l'utiliser
        clip.setFramePosition(0);  // Remettre au début
        clip.start();
    }
    }
    /** Boucle la lecture du fichier audio.
     * Utile pour les musiques principales.
     */
    public void loop() {
    if (clip != null) {  // Vérifier que le clip n'est pas null
        clip.loop(Clip.LOOP_CONTINUOUSLY);
    }
    }
    /** Arrête la lecture du fichier audio. */
    public void stop() {
    if (clip != null) {  
        clip.stop();
    }
    }
    }