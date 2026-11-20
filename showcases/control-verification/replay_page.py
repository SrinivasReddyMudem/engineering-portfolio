"""Verified recorded replay only. No compiler, shell, network or model execution."""
from pathlib import Path
import hashlib,json,re

PUBLIC_FILES='https://github.com/SrinivasReddyMudem/engineering-portfolio/blob/feature/control-verification-streamlit/showcases/control-verification/presentation/'

def load_page(directory):
 directory=Path(directory)
 manifest=json.loads((directory/'manifest.json').read_text())
 for name,digest in manifest.items():
  path=(directory/name).resolve()
  if Path(name).name!=name or not path.is_relative_to(directory.resolve()):raise ValueError('Invalid replay asset path')
  if hashlib.sha256(path.read_bytes()).hexdigest()!=digest:raise ValueError('Replay integrity failure: '+name)
 page=(directory/'index.html').read_text(encoding='utf-8')
 for name in ('animation.css','four-panel-style.css'):
  page=page.replace('<link rel="stylesheet" href="'+name+'">','<style>'+(directory/name).read_text(encoding='utf-8')+'</style>')
 page=page.replace('<script src="animation.js"></script>','<script>'+(directory/'animation.js').read_text(encoding='utf-8')+'</script>')
 for name in ('review.html','review.md','evidence.json','verification-evidence.json','fault-definitions.json'):
  page=page.replace('href="'+name+'"','target="_blank" rel="noopener noreferrer" href="'+PUBLIC_FILES+name+'"')
 if re.search(r'<(?:script|link)[^>]+(?:src|href)="(?!https:)',page):raise ValueError('Unresolved replay dependency')
 return page
