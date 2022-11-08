/**
 * 
 * @author ChiangWei
 * @date 2020/01/12
 *
 */

public interface Subject {
	public void registerObserver(Observer o);
	public void removeObserver(Observer o);
	public void notifyObservers();
}
