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
// �۩w�q��l��
// import �ɤJ�ۤv�� KeyManager
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
// An abstract representation of file and directory pathnames.
import java.io.File;

public class TinkUtil {
	
	// �ϥ� Tink �����Ҧ���y�ӹ�{��l��
	public void register01() {
		try {
			TinkConfig.register();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	// �ϥ� AEAD ��y��{
	public void register02() {
		try {
			AeadConfig.register();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	// �۩w�q��l��
	public void register03() {
		// Registry.registerKeyManager(new KeyManager());
	}
	
	// AEAD �[�K�ѱK
	// associated data to be authenticated
	public void aead(byte[] plaintext, byte[] associated) {
		try {
			// 1. �t�m�ͦ��K�_��
			KeysetHandle keysetHandle = KeysetHandle.generateNew(AeadKeyTemplates.AES128_GCM);
			// 2. �ϥ� Key ����ҿ��y�����
			Aead aead = AeadFactory.getPrimitive(keysetHandle);
			// 3. �ϥέ�y�����[�K
			byte[] ciphertext = aead.encrypt(plaintext, associated);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	// �ͦ��]�t�H���ͦ��� AES 128 - GCM �K�_���K�_��
	public void createKeySet() {
		try {
			// pre-generated templates
			KeyTemplate keyTemplate = AeadKeyTemplates.AES128_GCM;
			KeysetHandle keysetHandle = KeysetHandle.generateNew(keyTemplate);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	// �ͦ��K�_��A�N��O�s���x�s�t�Τ��A�H�g�J��󬰨�
	public void save2File() {
		try {
			// �Ы� AES ������ keysetHandle
			KeysetHandle keysetHandle = KeysetHandle.generateNew(AeadKeyTemplates.AES128_GCM);
			// �g�J json ���
			String keysetFilename = "my_keyset.json";
			CleartextKeysetHandle.write(keysetHandle, JsonKeysetWriter.withFile(new File(keysetFilename)));
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	// �ϥ� Google Cloud KMS key �ӹ� key �[�K
	public void save2FileBaseKMS() {
		try {
			// �Ы� AES ������ keysetHandle
			KeysetHandle keysetHandle = KeysetHandle.generateNew(AeadKeyTemplates.AES128_GCM);
			// �g�J json ���
			String keysetFilename = "my_keyset.json";
			// �ϥ� gcp-kms �覡��K�_�[�K
			String masterKeyUri = "gcp-kms://projects/tink-examples/locations/global/keyRings/foo/cryptoKeys/bar";
			keysetHandle.write(JsonKeysetWriter.withFile(new File(keysetFilename)), new GcpKmsClient().getAead(masterKeyUri));
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	// �ϥ� KeysetHandle �[���[�K���K�_��
	public void loadKeySet() {
		try {
			String keysetFilename = "my_keyset.json";
			// �ϥ� aws-kms �覡��K�_�[�K
			String masterKeyUri = "aws-kms://arn:aws:kms:us-east-1:00708442586:key/84a65985-f868-4bfc-83c2-366618acf147";
			KeysetHandle keysetHandle = KeysetHandle.read(JsonKeysetReader.withFile(new File(keysetFilename)), new AwsKmsClient().getAead(masterKeyUri));
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	// �[�����媺�K�_���A�ϥ� CleartextKeysetHandle
	public void loadCleartextKeyset() {
		try {
			String keysetFilename = "my_keyset.json";
			KeysetHandle keysetHandle = CleartextKeysetHandle.read(JsonKeysetReader.withFile(new File(keysetFilename)));
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
