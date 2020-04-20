/**
 * 
 * @author ChiangWei
 * @date 2020/02/17
 *
 */

package Sample2;

public class Stereo {
	String location;
	
	public Stereo(String location) {
		this.location = location;
	}
	
	public void on() {
		System.out.println(location + " stereo is on");
	}
	
	public void setCD() {
		System.out.println(location + " stereo is set for CD input");
	}
	
	public void setVolume(int i) {
		System.out.println(location + " stereo volume set to " + i);
	}
	
	public void off() {
		System.out.println(location + " stereo is off");
	}
}
