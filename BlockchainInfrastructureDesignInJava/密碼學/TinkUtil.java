/**
 * 
 * @author ChiangWei
 * @date 2020/4/29
 *
 */

// Static methods and constants for registering with the Registry all instances of all key types supported in a particular release of Tink.
import com.google.crypto.tink.config.TinkConfig;
// Static methods and constants for registering with the Registry all instances of Aead key types supported in a particular release of Tink.
import com.google.crypto.tink.aead.AeadConfig;
// A global container of key managers and catalogues
import com.google.crypto.tink.Registry;
// 自定義初始化
// import 導入自己的 KeyManager

public class TinkUtil {
	
	// To register all key types provided in the latest Tink version one can do
	public void register01() {
		try {
			TinkConfig.register();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	// To register all Aead key types provided in the latest Tink version one can do
	public void register02() {
		try {
			AeadConfig.register();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	// 自定義初始化
	public void register03() {
		// Registry.registerKeyManager(new KeyManager());
	}
}
