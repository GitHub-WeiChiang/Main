/**
 * 
 * @author ChiangWei
 * @date 2020/01/12
 *
 */

public class WeatherStation {
	public static void main(String[] args) {
		WeatherData weatherData = new WeatherData();
		CurrentConditionsDisplay currentDisplay = new CurrentConditionsDisplay(weatherData);
		weatherData.setMeasurements(80, 65, 30.4f);
		
		WeatherDataObservable weatherDataObservable = new WeatherDataObservable();
		CurrentConditionsDisplayObserver currentConditionsDisplayObserver = new CurrentConditionsDisplayObserver(weatherDataObservable);
		weatherDataObservable.setMeasurements(80, 65, 30.4f);
	}
}