/**
 * 
 * @author ChiangWei
 * @date 2020/2/18
 *
 */

public class HomeTheaterTestDrive {
	public static void main(String[] args) {
		Amplifier amp = new Amplifier();
		DvdPlayer dvd = new DvdPlayer();
		Projector projector = new Projector();
		TheaterLights lights = new TheaterLights();
		Screen screen = new Screen();
		PopcornPopper popper = new PopcornPopper();
		
		HomeTheaterFacade homeTheater = new HomeTheaterFacade(amp, dvd, projector, screen, lights, popper);
		homeTheater.watchMovie("Raiders of the Lost Ark");
		homeTheater.endMovie();
	}
}
