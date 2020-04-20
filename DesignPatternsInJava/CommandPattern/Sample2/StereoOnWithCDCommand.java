/**
 * 
 * @author ChiangWei
 * @date 2020/02/17
 *
 */

package Sample2;

public class StereoOnWithCDCommand implements Command {
	Stereo stereo;
	
	public StereoOnWithCDCommand(Stereo stereo) {
		this.stereo = stereo;
	}
	
	public void execute() {
		stereo.on();
		stereo.setCD();
		stereo.setVolume(11);
	}
	
	public void undo() {
		stereo.off();
	}
}
