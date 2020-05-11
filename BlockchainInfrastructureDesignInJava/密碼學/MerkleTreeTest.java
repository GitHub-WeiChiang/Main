/**
 * 
 * @author ChiangWei
 * @date 2020/5/11
 *
 */

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class MerkleTreeTest {

	@Test
	void MerkleTreeTest() {
		// case1: List<String> contents = null;
		List<String> contents = null;
		assertEquals(new MerkleTree(contents).getList(), null);
		assertEquals(new MerkleTree(contents).getRoot(), null);
		
		// case2: List<String> contents = new ArrayList<>();
		contents = new ArrayList<>();
		assertEquals(new MerkleTree(contents).getList(), null);
		assertEquals(new MerkleTree(contents).getRoot(), null);
		
		// case3: List<String> contents 有內容
		contents = Arrays.asList("區塊鏈", "人工智能", "腦科學", "K12 教育全球優質公司");
		assertEquals(new MerkleTree(contents).getRoot().getHash(), "265d6a9a7b08d85349c899b5faf26b6ac0655b1746ec41a582bb265111d4d7db");
		assertEquals(new MerkleTree(contents).getRoot().getName(), "(([節點: 區塊鏈]和[節點: 人工智能]的父節點)和([節點: 腦科學]和[節點: K12 教育全球優質公司]的父節點)的父節點)");
	
		new MerkleTree(contents).traverseTreeNodes();
	}

}
