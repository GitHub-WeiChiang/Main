package course.c06;

public class Employee {

	private String name;
	private int id;
	private Address address;

	public String getName() {
		return this.name;
	}

	public void setName(String nm) {
		this.name = nm;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public Address getAddress() {
		return address;
	}

	public void setAddress(Address address) {
		this.address = address;
	}

	@Override
	public String toString() {
		return "【ID=" + id + ",Name=" + name + ",Address=" + address + "】";
	}

}