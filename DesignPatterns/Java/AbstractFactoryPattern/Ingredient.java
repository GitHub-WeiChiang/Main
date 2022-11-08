/**
 * 
 * @author ChiangWei
 * @date 2020/02/12
 *
 */

public interface Ingredient {}

interface Dough extends Ingredient {}
class ThinCrustDough implements Dough {}

interface Sauce extends Ingredient {}
class MarinaraSauce implements Sauce {}

interface Cheese extends Ingredient {}
class ReggianoCheese implements Cheese {}

interface Veggies extends Ingredient {}
class Garlic implements Veggies {}
class Onion implements Veggies {}
class Mushroom implements Veggies {}
class RedPepper implements Veggies {}

interface Pepperoni extends Ingredient {}
class SlicedPepperoni implements Pepperoni {}

interface Clams extends Ingredient {}
class FreshClams implements Clams {}