/**
 * 
 * @author ChiangWei
 * @date 2020/3/11
 *
 */

public class DrawingAnEnglishRuler {
	public static void main(String[] args) {
		drawRuler(3, 2);
	}
	
	public static void drawRuler(int nlnches, int majorLength) {
		drawLine(majorLength, 0);
		for (int i = 1; i <= nlnches; i++) {
			drawInterval(majorLength - 1);
			drawLine(majorLength, i);
		}
	}
	
	private static void drawInterval(int centralLength) {
		if (centralLength >= 1) {
			drawInterval(centralLength - 1);
			drawLine(centralLength);
			drawInterval(centralLength - 1);
		}
	}
	
	private static void drawLine(int tickLength, int tickLabel) {
		for (int i = 0; i < tickLength; i++) System.out.print("-");
		if (tickLabel >= 0) System.out.print(" " + tickLabel);
		System.out.println("");
	}
	
	private static void drawLine(int tickLength) {
		drawLine(tickLength, -1);
	}
}
