/**
 * 
 * @author ChiangWei
 * @date 2020/02/17
 *
 */

package Sample4;

public class CeilingFan {
	String location;
	
	public CeilingFan(String location) {
		this.location = location;
	}
	
	public void on() {
		System.out.println(location + " ceiling fan is on high");
	}
	
	public void off() {
		System.out.println(location + " ceiling fan is off");
	}
}
