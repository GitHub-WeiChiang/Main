/**
 * 
 * @author ChiangWei
 * @date 2020/02/10
 *
 */

public abstract class Beverage {
	String description = "Unknown Beverage";
	
	public String getDescription() {
		return description;
	}
	
	public abstract double cost();
}
