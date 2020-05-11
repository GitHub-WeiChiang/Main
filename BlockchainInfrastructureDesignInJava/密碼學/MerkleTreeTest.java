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
		
		// case3: List<String> contents �����e
		contents = Arrays.asList("�϶���", "�H�u����", "�����", "K12 �Ш|���y�u�褽�q");
		assertEquals(new MerkleTree(contents).getRoot().getHash(), "265d6a9a7b08d85349c899b5faf26b6ac0655b1746ec41a582bb265111d4d7db");
		assertEquals(new MerkleTree(contents).getRoot().getName(), "(([�`�I: �϶���]�M[�`�I: �H�u����]�����`�I)�M([�`�I: �����]�M[�`�I: K12 �Ш|���y�u�褽�q]�����`�I)�����`�I)");
	
		new MerkleTree(contents).traverseTreeNodes();
	}

}
