/**
 * 
 * @author ChiangWei
 * @date 2020/4/27
 *
 */

// A private key. The purpose of this interface is to group (and provide type safety for) all private key interfaces.
import java.security.PrivateKey;
// A public key. This interface contains no methods or constants. It merely serves to group (and provide type safety for) all public key interfaces.
import java.security.PublicKey;
//Testing framework for Java
import org.testng.util.Strings;

// 字符集工具類
import cn.hutool.core.util.CharsetUtil;
// 字符串工具類
import cn.hutool.core.util.StrUtil;
// 安全相關工具類，加密分為三種:
// 1、對稱加密（symmetric），例如：AES、DES等
// 2、非對稱加密（asymmetric），例如：RSA、DSA等
// 3、摘要加密（digest），例如：MD5、SHA-1、SHA-256、HMAC等
import cn.hutool.crypto.SecureUtil;
// 密鑰類型
import cn.hutool.crypto.asymmetric.KeyType;
// RSA公鑰/私鑰/簽名加密解密
// 由於非對稱加密速度極其緩慢，一般文件不使用它來加密而是使用對稱加密，非對稱加密算法可以用來對對稱加密的密鑰加密，這樣保證密鑰的安全也就保證了數據的安全
import cn.hutool.crypto.asymmetric.RSA;
// AES加密算法實現
// 高級加密標準（英語：Advanced Encryption Standard，縮寫：AES），在密碼學中又稱Rijndael加密法對於Java中AES的默認模式是：AES/ECB/PKCS5Padding，如果使用CryptoJS，請調整為：padding: CryptoJS.pad.Pkcs7
import cn.hutool.crypto.symmetric.AES;
// DES加密算法實現
// DES全稱為Data Encryption Standard，即數據加密標準，是一種使用密鑰加密的塊算法Java中默認實現為：DES/CBC/PKCS5Padding
import cn.hutool.crypto.symmetric.DES;

public class DeEnCoderHutoolUtil {

}
