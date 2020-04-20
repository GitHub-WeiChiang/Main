/**
 * 
 * @author ChiangWei
 * @date 2020/02/17
 *
 */

package Sample2;

public class RemoteLoader {
	public static void main(String[] args) {
		RemoteControl remoteControl = new RemoteControl();
		
		Light livingRoomLight = new Light("Living Room");
		Light kitchenLight = new Light("kitchen");
		CeilingFan ceilingFan = new CeilingFan("Living Room");
		Stereo stereo = new Stereo("Living Room");
		
		LightOnCommand livingRoomLightOn = new LightOnCommand(livingRoomLight);
		LightOffCommand livingRoomLightOff = new LightOffCommand(livingRoomLight);
		
		LightOnCommand kitchenLightOn = new LightOnCommand(kitchenLight);
		LightOffCommand lkitchenLightOff = new LightOffCommand(kitchenLight);
		
		CeilingFanOnCommand ceilingFanOn = new CeilingFanOnCommand(ceilingFan);
		CeilingFanOffCommand ceilingFanOff = new CeilingFanOffCommand(ceilingFan);
		
		StereoOnWithCDCommand stereoOnWithCD = new StereoOnWithCDCommand(stereo);
		StereoOffWithCDCommand stereoOffWithCD = new StereoOffWithCDCommand(stereo);
		
		remoteControl.setCommand(0, livingRoomLightOn, livingRoomLightOff);
		remoteControl.setCommand(1, kitchenLightOn, lkitchenLightOff);
		remoteControl.setCommand(2, ceilingFanOn, ceilingFanOff);
		remoteControl.setCommand(3, stereoOnWithCD, stereoOffWithCD);
		
		System.out.println(remoteControl);
		
		remoteControl.onButtonWasPushed(0);
		remoteControl.offButtonWasPushed(0);
		remoteControl.onButtonWasPushed(1);
		remoteControl.offButtonWasPushed(1);
		remoteControl.onButtonWasPushed(2);
		remoteControl.offButtonWasPushed(2);
		remoteControl.onButtonWasPushed(3);
		remoteControl.offButtonWasPushed(3);
		
		System.out.println("==================================================");
		
		RemoteControl remoteControl2 = new RemoteControl();
		remoteControl2.setCommand(0, livingRoomLightOn, livingRoomLightOff);
		remoteControl2.onButtonWasPushed(0);
		remoteControl2.offButtonWasPushed(0);
		System.out.println(remoteControl2);
		remoteControl2.undoButtonWasPushed();
		remoteControl2.offButtonWasPushed(0);
		remoteControl2.onButtonWasPushed(0);
		System.out.println(remoteControl2);
		remoteControl2.undoButtonWasPushed();
	}
}
