/**
 * 
 * @author ChiangWei
 * @date 2020/02/11
 *
 */

public class NYPizzaStore extends PizzaStore {
	Pizza createPizza(String item) {
		if (item.equals("cheese")) {
			return new NYStyleCheesePizza();
		}
//		else if () {
//			
//		}
		else return null;
	}
}
