/**
 * 
 * @author ChiangWei
 * @date 2020/02/17
 *
 */

package Sample2;

public class LightOffCommand implements Command {
	Light light;
	
	public LightOffCommand(Light light) {
		this.light = light;
	}
	
	public void execute() {
		light.off();
	}
	
	public void undo() {
		light.on();
	}
}
