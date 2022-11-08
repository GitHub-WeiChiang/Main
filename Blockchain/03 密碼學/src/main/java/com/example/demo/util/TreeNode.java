/**
 * 
 * @author ChiangWei
 * @date 2022/03/30
 *
 */

package com.example.demo.util;

// 樹節點定義
public class TreeNode {
	// 二叉樹的左孩子
	private TreeNode left;
	// 二叉樹的右孩子
	private TreeNode right;
	// 二叉樹中節點的數據
	private String data;
	// 二叉樹中節點的數據對應的哈希值，此處採用 SHA - 256 算法處理
	private String hash;
	// 節點名稱
	private String name;
	
	// 構造函數 1
	public TreeNode() {
		
	}
	
	// 構造函數 2
	public TreeNode(String data) {
		this.data = data;
		this.hash = SHAUtil.sha256BasedHutool(data);
		this.name = "[節點: " + data + "]";
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
