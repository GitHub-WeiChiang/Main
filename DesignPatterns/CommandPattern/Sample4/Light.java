/**
 * 
 * @author ChiangWei
 * @date 2020/02/17
 *
 */

package Sample4;

public class Light {
	String location;
	
	public Light(String location) {
		this.location = location;
	}
	
	public void on() {
		System.out.println(location + " light is on");
	}
	
	public void off() {
		System.out.println(location + " light is off");
	}
}
