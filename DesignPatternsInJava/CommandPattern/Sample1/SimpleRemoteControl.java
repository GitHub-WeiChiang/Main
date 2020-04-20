/**
 * 
 * @author ChiangWei
 * @date 2020/02/17
 *
 */

package Sample1;

public class SimpleRemoteControl {
	Command slot;
	
	public SimpleRemoteControl() {}
	
	public void setCommand(Command command) {
		slot = command;
	}
	
	public void buttonWasPressed() {
		slot.execute();
	}
}
