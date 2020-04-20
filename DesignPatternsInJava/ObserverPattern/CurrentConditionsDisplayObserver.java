/**
 * 
 * @author ChiangWei
 * @date 2020/01/12
 *
 */

import java.util.Observable;
import java.util.Observer;

public class CurrentConditionsDisplayObserver implements Observer, DisplayElement {
	Observable observable;
	private float temperature;
	private float humidity;
	
	public CurrentConditionsDisplayObserver(Observable observable) {
		this.observable = observable;
		observable.addObserver(this);
	}

	@Override
	public void update(Observable obs, Object arg) {
		if (obs instanceof WeatherDataObservable) {
			WeatherDataObservable weatherDataObservable = (WeatherDataObservable)obs;
			this.temperature = weatherDataObservable.getTemperature();
			this.humidity = weatherDataObservable.getHumidity();
			display();
		}
	}
	
	@Override
	public void display() {
		System.out.println("Current condition: " + temperature + "F degrees and " + humidity + "% humidity");
	}
}
