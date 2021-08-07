/**
 * 
 * @author ChiangWei
 * @date 2020/01/11
 *
 */

public class MuteQuack implements QuackBehavior {
	@Override
	public void quack() {
		System.out.println("<< Silence >>");
	}
}
