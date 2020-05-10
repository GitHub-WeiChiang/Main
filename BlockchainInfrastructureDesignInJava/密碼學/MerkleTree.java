/**
 * 
 * @author ChiangWei
 * @date 2020/5/10
 *
 */

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

// MerkleTree �غc�B�ͦ��ڸ`�I���ƭȪ��u����
public class MerkleTree {
	
	// TreeNode List
	private List<TreeNode> list;
	// �ڵ��I
	private TreeNode root;
	
	// �c�y���
	public MerkleTree(List<String> contents) {
		createMerkleTree(contents);
	}
	
	// �غc Merkle Tree
	private void createMerkleTree(List<String> contents) {
		// ��J���ūh���i�����B�z
		if (contents == null || contents.size() == 0) {
			return;
		}
		
		// ��l��
		list = new ArrayList<>();
		
		// �ھڼƾڳЫظ��l�`�I
		List<TreeNode> leafList = createLeafList(contents);
		list.addAll(leafList);
		
		// �Ыؤ��`�I
		List<TreeNode> parents = createParentList(leafList);
		list.addAll(parents);
		
		// �`���ЫئU�Ť��`�I�ܮڸ`�I
		while (parents.size() > 1) {
			List<TreeNode> temp = createParentList(parents);
			list.addAll(temp);
			parents = temp;
		}
		
		root = parents.get(0);
	}
	
	// �Ыؤ��`�I�C��
	private List<TreeNode> createParentList(List<TreeNode> leafList) {
		List<TreeNode> parents = new ArrayList<>();
		
		// ������
		if (leafList == null || leafList.size() == 0) {
			return parents;
		}
		
		int length = leafList.size();
		for (int i = 0; i < length - 1; i += 2) {
			TreeNode parent = createParentNode(leafList.get(i), leafList.get(i + i));
			parents.add(parent);
		}
		
		// �_�ƭӸ`�I�ɡA��W�B�z�̫�@�Ӹ`�I
		if (length % 2 != 0) {
			TreeNode parent = createParentNode(leafList.get(length - 1), null);
			parents.add(parent);
		}
		
		return parents;
	}
	
	// �Ыؤ��`�I
	private TreeNode createParentNode(TreeNode left, TreeNode right) {
		TreeNode parent = new TreeNode();
		
		parent.setLeft(left);
		parent.setRight(right);
		
		// �p�G right ���šA�d���`�I�����ƭȬ� left �����ƭ�
		String hash = left.getHash();
		if (right != null) {
			hash = SHAUtil.sha256BasedHutool(left.getHash() + right.getHash());
		}
		// hash �r�q�M data �r�q�P��
		parent.setData(hash);
		parent.setHash(hash);
		
		if (right != null) {
			parent.setName("(" + left.getName() + "�M" + right.getName() + "�����`�I)");
		} else {
			parent.setName("(�~�Ӹ`�I{" + left.getName() + "}�������`�I)");
		}
		
		return parent;
	}
	
	// �c�ظ��l�`�I�C��
	private List<TreeNode> createLeafList(List<String> contents) {
		List<TreeNode> leafList = new ArrayList<>();
		
		// ������
		if (contents == null || contents.size() == 0) {
			return leafList;
		}
		
		for (String content : contents) {
			TreeNode node = new TreeNode(content);
			leafList.add(node);
		}
		
		return leafList;
	}
	
	// �M����
	public void traverseTreeNodes() {
		Collections.reverse(list);
		TreeNode root = list.get(0);
		traverseTreeNodes(root);
	}
	
	private void traverseTreeNodes(TreeNode node) {
		System.out.println(node.getName());
		
		if (node.getLeft() != null) {
			traverseTreeNodes(node.getLeft());
		}
		
		if (node.getRight() != null) {
			traverseTreeNodes(node.getRight());
		}
	}
	
	public List<TreeNode> getList() {
		if (list == null) {
			return list;
		}
		Collections.reverse(list);
		return list;
	}
	
	public void setList(List<TreeNode> list) {
		this.list = list;
	}
	
	public TreeNode getRoot() {
		return root;
	}
	
	public void setRoot(TreeNode root) {
		this.root = root;
	}
	
}
