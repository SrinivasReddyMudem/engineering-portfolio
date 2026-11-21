/* Optional aggregate analytics. No credentials; inactive until the owner configures a site. */
(()=>{'use strict';
const site='https://engineerportfolio.goatcounter.com'; // Owner's verified https://<code>.goatcounter.com address.
if(location.hostname!=='srinivasreddymudem.github.io'||!location.pathname.startsWith('/engineering-portfolio/control-verification/'))return;
if(!/^https:\/\/[a-z0-9-]+\.goatcounter\.com$/.test(site))return;
const settings=new URLSearchParams(location.search);
if(settings.get('analytics')==='off'){localStorage.setItem('portfolio-analytics-off','1');return;}
if(settings.get('analytics')==='on')localStorage.removeItem('portfolio-analytics-off');
if(localStorage.getItem('portfolio-analytics-off')==='1')return;
const once=new Set();
function event(name){if(once.has(name)||!window.goatcounter||typeof window.goatcounter.count!=='function')return;once.add(name);window.goatcounter.count({path:'control-'+name,title:name,event:true});}
const script=document.createElement('script');script.async=true;script.src='https://gc.zgo.at/count.js';script.dataset.goatcounter=site+'/count';document.head.append(script);
// Only aggregate actions; never send source, code, names or input values.
for(const [id,name] of [['play','walkthrough-start'],['show-defect','defect-verification-start'],['show-repair','repair-verification-start']]){const el=document.getElementById(id);if(el)el.addEventListener('click',()=>event(name));}
})();
