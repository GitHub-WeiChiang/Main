/**
 * 
 * @author ChiangWei
 * @date 2020/5/10
 *
 */

// ��`�I�w�q
public class TreeNode {
	// �G�e�𪺥��Ĥl
	private TreeNode left;
	// �G�e�𪺥k�Ĥl
	private TreeNode right;
	// �G�e�𤤫Ĥl�`�I���ƾ�
	private String data;
	// �G�e�𤤫Ĥl�`�I���ƾڹ��������ƭȡA���B�ĥ� SHA - 256 ��k�B�z
	private String hash;
	// �`�I�W��
	private String name;
	
	// �c�y��� 1
	public TreeNode() {
		
	}
	
	// �c�y��� 2
	public TreeNode(String data) {
		this.data = data;
		this.hash = SHAUtil.sha256BasedHutool(data);
		this.name = "[�`�I: " + data + "]";
	}
	
	public String getName() {
		return name;
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	public String getData() {
		return data;
	}
	
	public void setData(String data) {
		this.data = data;
	}
	
	public TreeNode getRight() {
		return right;
	}
	
	public void setRight(TreeNode right) {
		this.right = right;
	}
	
	public TreeNode getLeft() {
		return left;
	}
	
	public void setLeft(TreeNode left) {
		this.left = left;
	}
	
	public String getHash() {
		return hash;
	}
	
	public void setHash(String hash) {
		this.hash = hash;
	}
}
