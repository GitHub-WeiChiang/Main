/**
 * 
 * @author ChiangWei
 * @date 2020/02/12
 *
 */

public interface PizzaIngredientFactory {
	public Dough createDough();
	public Sauce  createSauce();
	public Cheese createCheese();
	public Veggies[] createVeggies();
	public Pepperoni createPepperoni();
	public Clams createClam();
}
