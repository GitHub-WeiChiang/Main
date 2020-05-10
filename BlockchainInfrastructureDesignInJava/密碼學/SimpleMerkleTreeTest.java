/**
 * 
 * @author ChiangWei
 * @date 2020/5/10
 *
 */

import static org.junit.jupiter.api.Assertions.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.junit.jupiter.api.Test;

class SimpleMerkleTreeTest {

	@Test
	void testGetMerkleNodeList() {
		// case1: List<String> contentList = null;
		List<String> contentList = null;
		assertEquals(SimpleMerkleTree.getMerkleNodeList(contentList).size(), 0);
		
		// case2: List<String> contentList = new ArrayList<>(); 但無內容
		contentList = new ArrayList<>();
		assertEquals(SimpleMerkleTree.getMerkleNodeList(contentList).size(), 0);
		
		// case3: contentList 有內容填充
		contentList = Arrays.asList("區塊鏈", "人工智能", "腦科學", "K12 教育全球優質公司");
		assertEquals(SimpleMerkleTree.getMerkleNodeList(contentList).size(), 2);
	}
	
	@Test
	void testGetTreeNodeHash() {
		// case1: List<Stirng> contentList = null;
		List<String> contentList = null;
		assertEquals(SimpleMerkleTree.getTreeNodeHash(contentList), null);
		
		// case2: List<String> contentList = new ArrayList<>(); 但無內容
		contentList = new ArrayList<>();
		assertEquals(SimpleMerkleTree.getTreeNodeHash(contentList), null);
		
		// case3: contentList 有內容填充
		contentList = Arrays.asList("區塊鏈", "人工智能", "腦科學", "K12 教育全球優質公司");
		assertEquals(SimpleMerkleTree.getTreeNodeHash(contentList), "76f61657c583ca3f783b092d04f7b6899a916323086102e3f0bf3f203432ee95");
	}

}
