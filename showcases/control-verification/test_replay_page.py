from pathlib import Path
import tempfile,shutil,unittest,json
from replay_page import load_page

class ReplayTests(unittest.TestCase):
 def test_verified_assets_are_self_contained(self):
  page=load_page(Path(__file__).parent/'presentation')
  self.assertIn('const panelRecordings=',page)
  self.assertNotIn('src="animation.js"',page)
  self.assertNotIn('chatgpt.site',page)
 def test_modified_assets_rejected(self):
  with tempfile.TemporaryDirectory() as folder:
   target=Path(folder)/'presentation';shutil.copytree(Path(__file__).parent/'presentation',target)
   with (target/'animation.js').open('a') as out:out.write('modified')
   with self.assertRaisesRegex(ValueError,'integrity'):load_page(target)
 def test_missing_assets_rejected(self):
  with tempfile.TemporaryDirectory() as folder:
   target=Path(folder)/'presentation';shutil.copytree(Path(__file__).parent/'presentation',target);(target/'animation.css').unlink()
   with self.assertRaises(OSError):load_page(target)
if __name__=='__main__':unittest.main()
