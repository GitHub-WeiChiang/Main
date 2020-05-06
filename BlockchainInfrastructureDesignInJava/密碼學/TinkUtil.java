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
// Interface for Authenticated Encryption with Associated Data (AEAD).
import com.google.crypto.tink.Aead;
// A KeysetHandle provides abstracted access to Keyset, to limit the exposure of actual protocol buffers that hold sensitive key material.
import com.google.crypto.tink.KeysetHandle;
// A KeysetReader knows how to read a Keyset or an EncryptedKeyset from some source.
import com.google.crypto.tink.KeysetReader;
// Static methods for obtaining Aead instances.
import com.google.crypto.tink.aead.AeadFactory;
// Pre-generated KeyTemplate for Aead keys.
import com.google.crypto.tink.aead.AeadKeyTemplates;
// KeyTemplate
import com.google.crypto.tink.proto.KeyTemplate;
// Static methods for reading or writing cleartext keysets.
import com.google.crypto.tink.CleartextKeysetHandle;
// A KeysetWriter that can write to some source cleartext or encrypted keysets in proto JSON format.
import com.google.crypto.tink.JsonKeysetWriter;
// A KeysetReader that can read from source source cleartext or encrypted keysets in proto JSON format.
import com.google.crypto.tink.JsonKeysetReader;
// An implementation of KmsClient for Google Cloud KMS.
import com.google.crypto.tink.integration.gcpkms.GcpKmsClient;
// An implementation of KmsClient for AWS KMS.
import com.google.crypto.tink.integration.awskms.AwsKmsClient;
// Digital Signatures provide functionality of signing data and verification of the signatures.
import com.google.crypto.tink.PublicKeySign;
// Digital Signatures provide functionality of signing data and verification of the signatures.
import com.google.crypto.tink.PublicKeyVerify;
// 用於獲取數位簽章的加簽 primitive 實例
import com.google.crypto.tink.signature.PublicKeySignFactory;
// 用於獲取數位簽章的驗簽 primitive 實例
import com.google.crypto.tink.signature.PublicKeyVerifyFactory;
// Pre-generated KeyTemplate for PublicKeySign and PublicKeyVerify.
import com.google.crypto.tink.signature.SignatureKeyTemplates;
// An abstract representation of file and directory pathnames.
import java.io.File;

public class TinkUtil {
	
	// 使用 Tink 中的所有原語來實現初始化
	public void register01() {
		try {
			TinkConfig.register();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	// 使用 AEAD 原語實現
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
	
	// AEAD 加密解密
	// associated data to be authenticated
	public void aead(byte[] plaintext, byte[] associated) {
		try {
			// 1. 配置生成密鑰集
			KeysetHandle keysetHandle = KeysetHandle.generateNew(AeadKeyTemplates.AES128_GCM);
			// 2. 使用 Key 獲取所選原語的實例
			Aead aead = AeadFactory.getPrimitive(keysetHandle);
			// 3. 使用原語完成加密
			byte[] ciphertext = aead.encrypt(plaintext, associated);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	// 生成包含隨機生成的 AES 128 - GCM 密鑰的密鑰集
	public void createKeySet() {
		try {
			// pre-generated templates
			KeyTemplate keyTemplate = AeadKeyTemplates.AES128_GCM;
			KeysetHandle keysetHandle = KeysetHandle.generateNew(keyTemplate);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	// 生成密鑰後，將其保存到儲存系統中，以寫入文件為例
	public void save2File() {
		try {
			// 創建 AES 對應的 keysetHandle
			KeysetHandle keysetHandle = KeysetHandle.generateNew(AeadKeyTemplates.AES128_GCM);
			// 寫入 json 文件
			String keysetFilename = "my_keyset.json";
			CleartextKeysetHandle.write(keysetHandle, JsonKeysetWriter.withFile(new File(keysetFilename)));
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	// 使用 Google Cloud KMS key 來對 key 加密
	public void save2FileBaseKMS() {
		try {
			// 創建 AES 對應的 keysetHandle
			KeysetHandle keysetHandle = KeysetHandle.generateNew(AeadKeyTemplates.AES128_GCM);
			// 寫入 json 文件
			String keysetFilename = "my_keyset.json";
			// 使用 gcp-kms 方式對密鑰加密
			String masterKeyUri = "gcp-kms://projects/tink-examples/locations/global/keyRings/foo/cryptoKeys/bar";
			keysetHandle.write(JsonKeysetWriter.withFile(new File(keysetFilename)), new GcpKmsClient().getAead(masterKeyUri));
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	// 使用 KeysetHandle 加載加密的密鑰集
	public void loadKeySet() {
		try {
			String keysetFilename = "my_keyset.json";
			// 使用 aws-kms 方式對密鑰加密
			String masterKeyUri = "aws-kms://arn:aws:kms:us-east-1:00708442586:key/84a65985-f868-4bfc-83c2-366618acf147";
			KeysetHandle keysetHandle = KeysetHandle.read(JsonKeysetReader.withFile(new File(keysetFilename)), new AwsKmsClient().getAead(masterKeyUri));
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	// 加載明文的密鑰集，使用 CleartextKeysetHandle
	public void loadCleartextKeyset() {
		try {
			String keysetFilename = "my_keyset.json";
			KeysetHandle keysetHandle = CleartextKeysetHandle.read(JsonKeysetReader.withFile(new File(keysetFilename)));
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	// 對稱密鑰加密，獲得和使用 AEAD
	public void aeadAES(byte[] plaintext, byte[] aad) {
		try {
			// 1. 創建 AES 對應的 keysetHandle
			KeysetHandle keysetHandle = KeysetHandle.generateNew(AeadKeyTemplates.AES128_GCM);
			// 2. 獲取私鑰
			Aead aead = AeadFactory.getPrimitive(keysetHandle);
			// 3. 用私鑰加密明文
			byte[] ciphertext = aead.encrypt(plaintext, aad);
			
			// 解秘密文
			byte[] decrypted = aead.decrypt(ciphertext, aad);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	// 數位簽章的簽名與驗證
	public void signatures(byte[] data) {
		try {
			// 簽名
			// 1. 創建 ESCSA 對應的 KeysetHandle 對象
			KeysetHandle privateKeysetHandle = KeysetHandle.generateNew(SignatureKeyTemplates.ECDSA_P256);
			// 2. 獲取私鑰
			PublicKeySign signer = PublicKeySignFactory.getPrimitive(privateKeysetHandle);
			// 3. 用私鑰簽名
			byte[] signature = signer.sign(data);
			
			// 驗證
			// 1. 獲取公鑰對應的 KeysetHandle 對象
			KeysetHandle publicKeysetHandle = privateKeysetHandle.getPublicKeysetHandle();
			// 2. 獲取私鑰
			PublicKeyVerify verifier = PublicKeyVerifyFactory.getPrimitive(publicKeysetHandle);
			// 3. 使用私鑰校驗簽名
			verifier.verify(signature, data);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
