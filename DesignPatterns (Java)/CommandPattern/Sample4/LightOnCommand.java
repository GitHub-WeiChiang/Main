/**
 * 
 * @author ChiangWei
 * @date 2020/02/17
 *
 */

package Sample4;

public class LightOnCommand implements Command {
	Light light;
	
	public LightOnCommand(Light light) {
		this.light = light;
	}
	
	public void execute() {
		light.on();
	}
	
	public void undo() {
		light.off();
	}
}
