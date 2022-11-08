/**
 * 
 * @author ChiangWei
 * @date 2020/02/11
 *
 */

public class ChicagoPizzaStore extends PizzaStore {
	Pizza createPizza(String item) {
		if (item.equals("cheese")) {
			return new ChicagoStyleCheesePizza();
		}
//		else if () {
//			
//		}
		else return null;
	}
}
