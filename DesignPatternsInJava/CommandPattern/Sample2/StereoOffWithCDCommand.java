/**
 * 
 * @author ChiangWei
 * @date 2020/02/17
 *
 */


package Sample2;

public class StereoOffWithCDCommand implements Command {
	Stereo stereo;
	
	public StereoOffWithCDCommand(Stereo stereo) {
		this.stereo = stereo;
	}
	
	public void execute() {
		stereo.off();
	}
	
	public void undo() {
		stereo.on();
		stereo.setCD();
		stereo.setVolume(11);
	}
}
