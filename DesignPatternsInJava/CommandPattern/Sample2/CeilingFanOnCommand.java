/**
 * 
 * @author ChiangWei
 * @date 2020/02/17
 *
 */

package Sample2;

public class CeilingFanOnCommand implements Command {
	CeilingFan ceilingFan;
	
	public CeilingFanOnCommand(CeilingFan ceilingFan) {
		this.ceilingFan = ceilingFan;
	}
	
	public void execute() {
		ceilingFan.on();
	}
	
	public void undo() {
		ceilingFan.off();
	}
}
