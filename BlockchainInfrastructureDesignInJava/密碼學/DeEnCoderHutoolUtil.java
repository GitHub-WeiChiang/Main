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

// �r�Ŷ��u����
import cn.hutool.core.util.CharsetUtil;
// �r�Ŧ�u����
import cn.hutool.core.util.StrUtil;
// �w�������u�����A�[�K�����T��:
// 1�B��٥[�K�]symmetric�^�A�Ҧp�GAES�BDES��
// 2�B�D��٥[�K�]asymmetric�^�A�Ҧp�GRSA�BDSA��
// 3�B�K�n�[�K�]digest�^�A�Ҧp�GMD5�BSHA-1�BSHA-256�BHMAC��
import cn.hutool.crypto.SecureUtil;
// �K�_����
import cn.hutool.crypto.asymmetric.KeyType;
// RSA���_/�p�_/ñ�W�[�K�ѱK
// �ѩ�D��٥[�K�t�׷���w�C�A�@���󤣨ϥΥ��ӥ[�K�ӬO�ϥι�٥[�K�A�D��٥[�K��k�i�H�Ψӹ��٥[�K���K�_�[�K�A�o�˫O�ұK�_���w���]�N�O�ҤF�ƾڪ��w��
import cn.hutool.crypto.asymmetric.RSA;
// AES�[�K��k��{
// ���ť[�K�зǡ]�^�y�GAdvanced Encryption Standard�A�Y�g�GAES�^�A�b�K�X�Ǥ��S��Rijndael�[�K�k���Java��AES���q�{�Ҧ��O�GAES/ECB/PKCS5Padding�A�p�G�ϥ�CryptoJS�A�нվ㬰�Gpadding: CryptoJS.pad.Pkcs7
import cn.hutool.crypto.symmetric.AES;
// DES�[�K��k��{
// DES���٬�Data Encryption Standard�A�Y�ƾڥ[�K�зǡA�O�@�بϥαK�_�[�K������kJava���q�{��{���GDES/CBC/PKCS5Padding
import cn.hutool.crypto.symmetric.DES;

public class DeEnCoderHutoolUtil {

}
