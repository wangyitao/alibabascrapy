# -*- coding: utf-8 -*-
# @Author  : FELIX
# @Date    : 2018/4/23 10:20
from selenium import webdriver

ii = '''
http://www.alibaba.com/product-detail/Brick-effect-self-adhesive-brick-pattern_60599387242.html
[16512:13084:0423/101859.688:ERROR:platform_sensor_reader_win.cc(242)] NOT IMPLEMENTED
[16512:13288:0423/101900.017:ERROR:platform_sensor_reader_win.cc(242)] NOT IMPLEMENTED
[16512:12028:0423/101900.723:ERROR:socket_dispatcher_host.cc(93)] Failed to resolve address for x., errorcode: -105
[16512:12028:0423/101900.724:ERROR:socket_dispatcher_host.cc(93)] Failed to resolve address for x., errorcode: -105
[16512:12028:0423/101900.725:ERROR:socket_dispatcher_host.cc(93)] Failed to resolve address for x., errorcode: -105
[16512:12028:0423/101900.725:ERROR:socket_dispatcher_host.cc(93)] Failed to resolve address for x., errorcode: -105
timeout
访问：http://www.alibaba.com/product-detail/Brick-effect-self-adhesive-brick-pattern_60599387242.html
timeout
访问：http://www.alibaba.com/product-detail/Brick-effect-self-adhesive-brick-pattern_60599387242.html
timeout
访问：http://www.alibaba.com/product-detail/Brick-effect-self-adhesive-brick-pattern_60599387242.html
<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" lang="en"><head><script async="" src="https://localhost.wwbizsrv.alibaba.com:4013/?callback=
jQuery183022496477029864193_1524449934075&amp;dmtrack_pageid=3cb072d40bb896fc5add428b162f04bf9681b5aa0f&amp;_=1524449935705"></script><script async=""
 src="https://localhost.wwbizsrv.alibaba.com:4013/?callback=jQuery183022496477029864193_1524449934074&amp;dmtrack_pageid=3cb072d40bb896fc5add428b162f0
4bf9681b5aa0f&amp;_=1524449935700"></script><script src="//cmap.alibaba.com/ml.html?callback=landing8978252&amp;cna=HjBkE2bITCQCATywctRfYiVV"></script
><script type="text/javascript" async="" src="https://assets.alicdn.com/g/alilog/oneplus/entry.js?t=211729"></script><script src="//g.alicdn.com/secur
ity/umscript/3.3.28/um.js" id="AWSC_umidPCModule"></script><script src="//aeu.alicdn.com/js/cj/107.js" id="AWSC_uabModule"></script><script async="" c
rossorigin="anonymous" src="https://g.alicdn.com/sd/pointman/js/pt2.js?_=423458"></script><script async="" defer="" crossorigin="anonymous" src="//i.a
licdn.com/sc-affiliate/sem-remarketing/??sem-remarketing.98174a0b.js"></script><script async="" src="//uaction.alicdn.com/js/uab.js"></script>
    <script type="text/javascript" async="" src="https://assets.alicdn.com/g/secdev/entry/index.js?t=211729" id="aplus-sufei"></script><script>/*! 201
8-04-20 19:37:05 v8.3.16 */
!function(e){function i(n){if(o[n])return o[n].exports;var r=o[n]={exports:{},id:n,loaded:!1};return e[n].call(r.exports,r,r.exports,i),r.loaded=!0,r.
exports}var o={};return i.m=e,i.c=o,i.p="",i(0)}([function(e,i){"use strict";var o=window,n=document;!function(){var e=2,r="ali_analytics";if(o[r]&amp
;&amp;o[r].ua&amp;&amp;e&lt;=o[r].ua.version)return void(i.info=o[r].ua);var t,a,d,s,c,u,h,l,m,b,f,v,p,w,g,x,z,O=o.navigator,k=O.appVersion,T=O&amp;&a
mp;O.userAgent||"",y=function(e){var i=0;return parseFloat(e.replace(/\./g,function(){return 0===i++?".":""}))},_=function(e,i){var o,n;i[o="trident"]
=.1,(n=e.match(/Trident\/([\d.]*)/))&amp;&amp;n[1]&amp;&amp;(i[o]=y(n[1])),i.core=o},N=function(e){var i,o;return(i=e.match(/MSIE ([^;]*)|Trident.*; r
v(?:\s|:)?([0-9.]+)/))&amp;&amp;(o=i[1]||i[2])?y(o):0},P=function(e){return e||"other"},M=function(e){function i(){for(var i=[["Windows NT 5.1","winXP
"],["Windows NT 6.1","win7"],["Windows NT 6.0","winVista"],["Windows NT 6.2","win8"],["Windows NT 10.0","win10"],["iPad","ios"],["iPhone;","ios"],["iP
od","ios"],["Macintosh","mac"],["Android","android"],["Ubuntu","ubuntu"],["Linux","linux"],["Windows NT 5.2","win2003"],["Windows NT 5.0","win2000"],[
"Windows","winOther"],["rhino","rhino"]],o=0,n=i.length;o&lt;n;++o)if(e.indexOf(i[o][0])!==-1)return i[o][1];return"other"}function r(e,i,n,r){var t,a
=o.navigator.mimeTypes;try{for(t in a)if(a.hasOwnProperty(t)&amp;&amp;a[t][e]==i){if(void 0!==n&amp;&amp;r.test(a[t][n]))return!0;if(void 0===n)return
!0}return!1}catch(e){return!1}}var t,a,d,s,c,u,h,l="",m=l,b=l,f=[6,9],v="{{version}}",p="&lt;!--[if IE "+v+"]&gt;&lt;s&gt;&lt;/s&gt;&lt;![endif]--&gt;
",w=n&amp;&amp;n.createElement("div"),g=[],x={webkit:void 0,edge:void 0,trident:void 0,gecko:void 0,presto:void 0,chrome:void 0,safari:void 0,firefox:
void 0,ie:void 0,ieMode:void 0,opera:void 0,mobile:void 0,core:void 0,shell:void 0,phantomjs:void 0,os:void 0,ipad:void 0,iphone:void 0,ipod:void 0,io
s:void 0,android:void 0,nodejs:void 0,extraName:void 0,extraVersion:void 0};if(w&amp;&amp;w.getElementsByTagName&amp;&amp;(w.innerHTML=p.replace(v,"")
,g=w.getElementsByTagName("s")),g.length&gt;0){for(_(e,x),s=f[0],c=f[1];s&lt;=c;s++)if(w.innerHTML=p.replace(v,s),g.length&gt;0){x[b="ie"]=s;break}!x.
ie&amp;&amp;(d=N(e))&amp;&amp;(x[b="ie"]=d)}else((a=e.match(/AppleWebKit\/*\s*([\d.]*)/i))||(a=e.match(/Safari\/([\d.]*)/)))&amp;&amp;a[1]?(x[m="webki
t"]=y(a[1]),(a=e.match(/OPR\/(\d+\.\d+)/))&amp;&amp;a[1]?x[b="opera"]=y(a[1]):(a=e.match(/Chrome\/([\d.]*)/))&amp;&amp;a[1]?x[b="chrome"]=y(a[1]):(a=e
.match(/\/([\d.]*) Safari/))&amp;&amp;a[1]?x[b="safari"]=y(a[1]):x.safari=x.webkit,(a=e.match(/Edge\/([\d.]*)/))&amp;&amp;a[1]&amp;&amp;(m=b="edge",x[
m]=y(a[1])),/ Mobile\//.test(e)&amp;&amp;e.match(/iPad|iPod|iPhone/)?(x.mobile="apple",a=e.match(/OS ([^\s]*)/),a&amp;&amp;a[1]&amp;&amp;(x.ios=y(a[1]
.replace("_","."))),t="ios",a=e.match(/iPad|iPod|iPhone/),a&amp;&amp;a[0]&amp;&amp;(x[a[0].toLowerCase()]=x.ios)):/ Android/i.test(e)?(/Mobile/.test(e
)&amp;&amp;(t=x.mobile="android"),a=e.match(/Android ([^\s]*);/),a&amp;&amp;a[1]&amp;&amp;(x.android=y(a[1]))):(a=e.match(/NokiaN[^\/]*|Android \d\.\d
|webOS\/\d\.\d/))&amp;&amp;(x.mobile=a[0].toLowerCase()),(a=e.match(/PhantomJS\/([^\s]*)/))&amp;&amp;a[1]&amp;&amp;(x.phantomjs=y(a[1]))):(a=e.match(/
Presto\/([\d.]*)/))&amp;&amp;a[1]?(x[m="presto"]=y(a[1]),(a=e.match(/Opera\/([\d.]*)/))&amp;&amp;a[1]&amp;&amp;(x[b="opera"]=y(a[1]),(a=e.match(/Opera
\/.* Version\/([\d.]*)/))&amp;&amp;a[1]&amp;&amp;(x[b]=y(a[1])),(a=e.match(/Opera Mini[^;]*/))&amp;&amp;a?x.mobile=a[0].toLowerCase():(a=e.match(/Oper
a Mobi[^;]*/))&amp;&amp;a&amp;&amp;(x.mobile=a[0]))):(d=N(e))?(x[b="ie"]=d,_(e,x)):(a=e.match(/Gecko/))&amp;&amp;(x[m="gecko"]=.1,(a=e.match(/rv:([\d.
]*)/))&amp;&amp;a[1]&amp;&amp;(x[m]=y(a[1]),/Mobile|Tablet/.test(e)&amp;&amp;(x.mobile="firefox")),(a=e.match(/Firefox\/([\d.]*)/))&amp;&amp;a[1]&amp;
&amp;(x[b="firefox"]=y(a[1])));t||(t=i());var z,O,T;if(!r("type","application/vnd.chromium.remoting-viewer")){z="scoped"in n.createElement("style"),T=
"v8Locale"in o;try{O=o.external||void 0}catch(e){}if(a=e.match(/360SE/))u="360";else if((a=e.match(/SE\s([\d.]*)/))||O&amp;&amp;"SEVersion"in O)u="sou
gou",h=y(a[1])||.1;else if((a=e.match(/Maxthon(?:\/)+([\d.]*)/))&amp;&amp;O){u="maxthon";try{h=y(O.max_version||a[1])}catch(e){h=.1}}else z&amp;&amp;T
?u="360se":z||T||!/Gecko\)\s+Chrome/.test(k)||x.opera||x.edge||(u="360ee")}(a=e.match(/TencentTraveler\s([\d.]*)|QQBrowser\/([\d.]*)/))?(u="tt",h=y(a[
2])||.1):(a=e.match(/LBBROWSER/))||O&amp;&amp;"LiebaoGetVersion"in O?u="liebao":(a=e.match(/TheWorld/))?(u="theworld",h=3):(a=e.match(/TaoBrowser\/([\
d.]*)/))?(u="taobao",h=y(a[1])||.1):(a=e.match(/UCBrowser\/([\d.]*)/))&amp;&amp;(u="uc",h=y(a[1])||.1),x.os=t,x.core=x.core||m,x.shell=b,x.ieMode=x.ie
&amp;&amp;n.documentMode||x.ie,x.extraName=u,x.extraVersion=h;var P=o.screen.width,M=o.screen.height;return x.resolution=P+"x"+M,x},S=function(e){func
tion i(e){return Object.prototype.toString.call(e)}function o(e,o,n){if("[object Function]"==i(o)&amp;&amp;(o=o(n)),!o)return null;var r={name:e,versi
on:""},t=i(o);if(o===!0)return r;if("[object String]"===t){if(n.indexOf(o)!==-1)return r}else if(o.exec){var a=o.exec(n);if(a)return a.length&gt;=2&am
p;&amp;a[1]?r.version=a[1].replace(/_/g,"."):r.version="",r}}var n={name:"other",version:""};e=(e||"").toLowerCase();for(var r=[["nokia",function(e){r
eturn e.indexOf("nokia ")!==-1?/\bnokia ([0-9]+)?/:/\bnokia([a-z0-9]+)?/}],["samsung",function(e){return e.indexOf("samsung")!==-1?/\bsamsung(?:[ \-](
?:sgh|gt|sm))?-([a-z0-9]+)/:/\b(?:sgh|sch|gt|sm)-([a-z0-9]+)/}],["wp",function(e){return e.indexOf("windows phone ")!==-1||e.indexOf("xblwp")!==-1||e.
indexOf("zunewp")!==-1||e.indexOf("windows ce")!==-1}],["pc","windows"],["ipad","ipad"],["ipod","ipod"],["iphone",/\biphone\b|\biph(\d)/],["mac","maci
ntosh"],["mi",/\bmi[ \-]?([a-z0-9 ]+(?= build|\)))/],["hongmi",/\bhm[ \-]?([a-z0-9]+)/],["aliyun",/\baliyunos\b(?:[\-](\d+))?/],["meizu",function(e){r
eturn e.indexOf("meizu")&gt;=0?/\bmeizu[\/ ]([a-z0-9]+)\b/:/\bm([0-9x]{1,3})\b/}],["nexus",/\bnexus ([0-9s.]+)/],["huawei",function(e){var i=/\bmediap
ad (.+?)(?= build\/huaweimediapad\b)/;return e.indexOf("huawei-huawei")!==-1?/\bhuawei\-huawei\-([a-z0-9\-]+)/:i.test(e)?i:/\bhuawei[ _\-]?([a-z0-9]+)
/}],["lenovo",function(e){return e.indexOf("lenovo-lenovo")!==-1?/\blenovo\-lenovo[ \-]([a-z0-9]+)/:/\blenovo[ \-]?([a-z0-9]+)/}],["zte",function(e){r
eturn/\bzte\-[tu]/.test(e)?/\bzte-[tu][ _\-]?([a-su-z0-9\+]+)/:/\bzte[ _\-]?([a-su-z0-9\+]+)/}],["vivo",/\bvivo(?: ([a-z0-9]+))?/],["htc",function(e){
return/\bhtc[a-z0-9 _\-]+(?= build\b)/.test(e)?/\bhtc[ _\-]?([a-z0-9 ]+(?= build))/:/\bhtc[ _\-]?([a-z0-9 ]+)/}],["oppo",/\boppo[_]([a-z0-9]+)/],["kon
ka",/\bkonka[_\-]([a-z0-9]+)/],["sonyericsson",/\bmt([a-z0-9]+)/],["coolpad",/\bcoolpad[_ ]?([a-z0-9]+)/],["lg",/\blg[\-]([a-z0-9]+)/],["android",/\ba
ndroid\b|\badr\b/],["blackberry",function(e){return e.indexOf("blackberry")&gt;=0?/\bblackberry\s?(\d+)/:"bb10"}]],t=0;t&lt;r.length;t++){var a=r[t][0
],d=r[t][1],s=o(a,d,e);if(s){n=s;break}}return n},E=1;try{t=M(T),a=S(T),d=t.os,s=t.shell,c=t.core,u=t.resolution,h=t.extraName,l=t.extraVersion,m=a.na
me,b=a.version,v=d?d+(t[d]?t[d]:""):"",p=s?s+parseInt(t[s]):"",w=c,g=u,x=h?h+(l?parseInt(l):""):"",z=m+b}catch(e){}f={p:E,o:P(v),b:P(p),w:P(w),s:g,mx:
x,ism:z},o[r]||(o[r]={}),o[r].ua||(o[r].ua={}),o.goldlog||(o.goldlog={}),i.info=o[r].ua=goldlog._aplus_client={version:e,ua_info:f}}()}]);/*! 2017-10-
31 20:15:15 v0.2.4 */
!function(t){function e(o){if(n[o])return n[o].exports;var i=n[o]={exports:{},id:o,loaded:!1};return t[o].call(i.exports,i,i.exports,e),i.loaded=!0,i.
exports}var n={};return e.m=t,e.c=n,e.p="",e(0)}([function(t,e,n){"use strict";!function(){var t=window.goldlog||(window.goldlog={});t._aplus_cplugin_
utilkit||(t._aplus_cplugin_utilkit={status:"init"},n(1).init(t),t._aplus_cplugin_utilkit.status="complete")}()},function(t,e,n){"use strict";var o=n(2
),i=n(4);e.init=function(t){t.setCookie=o.setCookie,t.getCookie=o.getCookie,t.on=i.on}},function(t,e,n){"use strict";var o=document,i=n(3),a=function(
t){var e=new RegExp("(?:^|;)\\s*"+t+"=([^;]+)"),n=o.cookie.match(e);return n?n[1]:""};e.getCookie=a;var r=function(t,e,n){n||(n={});var i=new Date;ret
urn n.expires&amp;&amp;("number"==typeof n.expires||n.expires.toUTCString)?("number"==typeof n.expires?i.setTime(i.getTime()+24*n.expires*60*60*1e3):i
=n.expires,e+="; expires="+i.toUTCString()):"session"!==n.expires&amp;&amp;(i.setTime(i.getTime()+63072e7),e+="; expires="+i.toUTCString()),e+="; path
="+(n.path?n.path:"/"),e+="; domain="+n.domain,o.cookie=t+"="+e,a(t)};e.setCookie=function(t,e,n){try{if(n||(n={}),n.domain)r(t,e,n);else for(var o=i.
getDomains(),a=0;a&lt;o.length;)n.domain=o[a],r(t,e,n)?a=o.length:a++}catch(t){}}},function(t,e){"use strict";e.getDomains=function(){var t=[];try{for
(var e=location.hostname,n=e.split("."),o=2;o&lt;=n.length;)t.push(n.slice(n.length-o).join(".")),o++}catch(t){}return t}},function(t,e){"use strict";
var n=window,o=document,i=!!o.attachEvent,a="attachEvent",r="addEventListener",c=i?a:r,u=function(t,e){var n=goldlog._$||{},o=n.meta_info||{},i=o.aplu
s_ctap||{};if(i&amp;&amp;"function"==typeof i.on)i.on(t,e);else{var a="ontouchend"in document.createElement("div"),r=a?"touchstart":"mousedown";s(t,r,
e)}},s=function(t,e,o){return"tap"===e?void u(t,o):void t[c]((i?"on":"")+e,function(t){t=t||n.event;var e=t.target||t.srcElement;"function"==typeof o&
amp;&amp;o(t,e)},!1)};e.on=s;var d=function(t){try{o.documentElement.doScroll("left")}catch(e){return void setTimeout(function(){d(t)},1)}t()},l=funct
ion(t){var e=0,n=function(){0===e&amp;&amp;t(),e++};"complete"===o.readyState&amp;&amp;n();var i;if(o.addEventListener)i=function(){o.removeEventListe
ner("DOMContentLoaded",i,!1),n()},o.addEventListener("DOMContentLoaded",i,!1),window.addEventListener("load",n,!1);else if(o.attachEvent){i=function()
{"complete"===o.readyState&amp;&amp;(o.detachEvent("onreadystatechange",i),n())},o.attachEvent("onreadystatechange",i),window.attachEvent("onload",n);
var a=!1;try{a=null===window.frameElement}catch(t){}o.documentElement.doScroll&amp;&amp;a&amp;&amp;d(n)}};e.DOMReady=function(t){l(t)},e.onload=functi
on(t){"complete"===o.readyState?t():s(n,"load",t)}}]);/*! 2017-12-19 12:10:24 v0.2.9 */
!function(o){function t(r){if(e[r])return e[r].exports;var a=e[r]={exports:{},id:r,loaded:!1};return o[r].call(a.exports,a,a.exports,t),a.loaded=!0,a.
exports}var e={};return t.m=o,t.c=e,t.p="",t(0)}([function(o,t,e){"use strict";!function(){var o=window.goldlog||(window.goldlog={});o._aplus_cplugin_
m||(o._aplus_cplugin_m=e(1).run())}()},function(o,t,e){"use strict";var r=e(2),a=e(3),n=e(4),s=navigator.sendBeacon?"post":"get";e(5).run(),t.run=func
tion(){return{status:"complete",do_tracker_jserror:function(o){try{var t=new n({logkey:o?o.logkey:"",ratio:o&amp;&amp;"number"==typeof o.ratio&amp;&am
p;o.ratio&gt;0?o.ratio:r.jsErrorRecordRatio}),e=["Message: "+o.message,"Error object: "+o.error].join(" - "),c=goldlog.spm_ab||[],i=location.hostname+
location.pathname;t.run({code:110,page:i,msg:"record_jserror_by"+s+"_"+o.message,spm_a:c[0],spm_b:c[1],c1:e,c2:o.filename,c3:location.protocol+"//"+i}
)}catch(o){a.logger({msg:o})}},do_tracker_lostpv:function(o){var t=!1;try{if(o&amp;&amp;o.page){var e=o.spm_ab?o.spm_ab.split("."):[],c="record_lostpv
_by"+s+"_"+o.msg,i=new n({ratio:o.ratio||r.lostPvRecordRatio});i.run({code:102,page:o.page,msg:c,spm_a:e[0],spm_b:e[1],c1:o.duration,c2:o.page_url}),t
=!0}}catch(o){a.logger({msg:o})}return t},do_tracker_obsolete_inter:function(o){var t=!1;try{if(o&amp;&amp;o.page){var e=o.spm_ab?o.spm_ab.split("."):
[],c="record_obsolete interface be called by"+s,i=new n({ratio:o.ratio||r.obsoleteInterRecordRatio});i.run({code:109,page:o.page,msg:c,spm_a:e[0],spm_
b:e[1],c1:o.interface_name,c2:o.interface_params}),t=!0}}catch(o){a.logger({msg:o})}return t},do_tracker_browser_support:function(o){var t=!1;try{if(o
&amp;&amp;o.page){var e=o.spm_ab?o.spm_ab.split("."):[],c=new n({ratio:o.ratio||r.browserSupportRatio}),i=goldlog._aplus_client||{},g=i.ua_info||{};c.
run({code:111,page:o.page,msg:o.msg+"_by"+s,spm_a:e[0],spm_b:e[1],c1:[g.o,g.b,g.w].join("_"),c2:o.etag||"",c3:o.cna||""}),t=!0}}catch(o){a.logger({msg
:o})}return t}}}},function(o,t){"use strict";t.lostPvRecordRatio="0.01",t.obsoleteInterRecordRatio="0.01",t.jsErrorRecordRatio="0.01",t.browserSupport
Ratio="0.01",t.goldlogQueueRatio="0.01"},function(o,t){"use strict";var e=function(o){var t=o.level||"warn";window.console&amp;&amp;window.console[t]&
amp;&amp;window.console[t](o.msg)};t.logger=e,t.assign=function(o,t){if("function"!=typeof Object.assign){var e=function(o){if(null===o)throw new Type
Error("Cannot convert undefined or null to object");for(var t=Object(o),e=1;e&lt;arguments.length;e++){var r=arguments[e];if(null!==r)for(var a in r)O
bject.prototype.hasOwnProperty.call(r,a)&amp;&amp;(t[a]=r[a])}return t};return e(o,t)}return Object.assign({},o,t)},t.makeCacheNum=function(){return M
ath.floor(268435456*Math.random()).toString(16)},t.obj2param=function(o){var t,e,r=[];for(t in o)o.hasOwnProperty(t)&amp;&amp;(e=""+o[t],r.push(t+"="+
encodeURIComponent(e)));return r.join("&amp;")}},function(o,t,e){var r=e(3),a={ratio:1,logkey:"fsp.1.1",gmkey:"",chksum:"H46747615"},n=function(o){o&a
mp;&amp;"object"==typeof o||(o=a),this.opts=o,this.opts.ratio=o.ratio||a.ratio,this.opts.logkey=o.logkey||a.logkey,this.opts.gmkey=o.gmkey||a.gmkey,th
is.opts.chksum=o.chksum||a.chksum},s=n.prototype;s.getRandom=function(){return Math.floor(100*Math.random())+1},s.run=function(o){var t,e,a={pid:"aplu
s",code:101,msg:"异常内容"},n="";try{var s=window.goldlog||{},c=s._$||{},i=c.meta_info||{},g=parseFloat(i["aplus-tracker-rate"]);if(t=this.opts||{},"n
umber"==typeof g&amp;&amp;g+""!="NaN"||(g=t.ratio),e=this.getRandom(),e&lt;=100*g){n="//gm.mmstat.com/"+t.logkey,o.rel=c.script_name+"@"+s.lver,o.type
=o.code,o.uid=encodeURIComponent(s.getCookie("cna")),o=r.assign(a,o);var l=r.obj2param(o);s.tracker=s.send(n,{cache:r.makeCacheNum(),gokey:l,logtype:"
2"},"POST")}}catch(o){r.logger({msg:"tracker.run() exec error: "+o})}},o.exports=n},function(o,t,e){"use strict";var r=e(6),a=function(o){var t=window
.goldlog||{},e=t._$=t._$||{},r=t.spm_ab?t.spm_ab.join("."):"0.0",a=e.send_pv_count||0;if(a&lt;1&amp;&amp;navigator&amp;&amp;navigator.sendBeacon){var
n=window.goldlog_queue||(window.goldlog_queue=[]),s=location.hostname+location.pathname;n.push({action:["goldlog","_aplus_cplugin_m","do_tracker_lostp
v"].join("."),arguments:[{page:s,page_url:location.protocol+"//"+s,duration:o,spm_ab:r,msg:"dom_state="+document.readyState}]})}};t.run=function(){var
 o=new Date;r.on(window,"beforeunload",function(){var t=new Date,e=t.getTime()-o.getTime();a(e)})}},function(o,t){"use strict";var e=window,r=document
,a=!!r.attachEvent,n="attachEvent",s="addEventListener",c=a?n:s;t.getIframeUrl=function(o){var t,e="//g.alicdn.com";return t=goldlog&amp;&amp;"functio
n"==typeof goldlog.getCdnPath?goldlog.getCdnPath()||e:e,(o||"https")+":"+t+"/alilog/aplus_cplugin/@@APLUS_CPLUGIN_VER/ls.html"},t.on=function(o,t,r){o
[c]((a?"on":"")+t,function(o){o=o||e.event;var t=o.target||o.srcElement;"function"==typeof r&amp;&amp;r(o,t)},!1)},t.checkLs=function(){var o;try{wind
ow.localStorage&amp;&amp;(localStorage.setItem("test_log_cna","1"),"1"===localStorage.getItem("test_log_cna")&amp;&amp;(localStorage.removeItem("test_
log_cna"),o=!0))}catch(t){o=!1}return o},t.tracker_iframe_status=function(o,t){var e=window.goldlog_queue||(window.goldlog_queue=[]),r=goldlog.spm_ab?
goldlog.spm_ab.join("."):"",a="createIframe_"+t.status+"_id="+o;t.msg&amp;&amp;(a+="_"+t.msg),e.push({action:"goldlog._aplus_cplugin_m.do_tracker_brow
ser_support",arguments:[{page:location.hostname+location.pathname,msg:a,browser_attr:navigator.userAgent,spm_ab:r,cna:t.duration||"",ratio:.01}]})},t.
tracker_ls_failed=function(){var o=window.goldlog_queue||(window.goldlog_queue=[]),t=goldlog.spm_ab?goldlog.spm_ab.join("."):"";o.push({action:"goldlo
g._aplus_cplugin_m.do_tracker_browser_support",arguments:[{page:location.hostname+location.pathname,msg:"donot support localStorage",browser_attr:navi
gator.userAgent,spm_ab:t}]})},t.processMsgData=function(o){var t={};try{t="string"==typeof o?JSON.parse(o):o,t||(t={})}catch(o){t={}}return t},t.do_pu
b_fn=function(o,t){var e=window.goldlog_queue||(window.goldlog_queue=[]);e.push({action:"goldlog.aplus_pubsub.publish",arguments:[o,t]}),e.push({actio
n:"goldlog.aplus_pubsub.cachePubs",arguments:[o,t]})}}]);/*! 2018-04-20 19:36:50 v8.3.16 */
!function(t){function e(o){if(n[o])return n[o].exports;var a=n[o]={exports:{},id:o,loaded:!1};return t[o].call(a.exports,a,a.exports,e),a.loaded=!0,a.
exports}var n={};return e.m=t,e.c=n,e.p="",e(0)}([function(t,e,n){t.exports=n(1)},function(t,e,n){"use strict";!function(){var t=function(){n(2);var e
=n(5),o=n(7);if(o.doPubMsg(["goldlogReady","running"]),document.getElementsByTagName("body").length){var a=window,r="g_tb_aplus_loaded";if(a[r])return
;a[r]=1,n(92).initGoldlog(e)}else setTimeout(function(){t()},50)};t()}()},function(t,e,n){"use strict";!function(){var t=window.goldlog||(window.goldl
og={}),e=n(3);t.aplus_pubsub||(t.aplus_pubsub=e.create())}()},function(t,e,n){"use strict";function o(t){if("function"!=typeof t)throw new TypeError(t
+" is not a function");return t}var a=n(4),r=function(t){for(var e=t.length,n=new Array(e-1),o=1;o&lt;e;o++)n[o-1]=t[o];return n},i=a.extend({create:f
unction(t){var e=new this;for(var n in t)e[n]=t[n];return e.handlers=[],e.pubs={},e},setHandlers:function(t){this.handlers=t},subscribe:function(t,e){
o(e);var n=this,a=n.pubs||{};if(a[t]){var r=a[t]();e.apply(n,r)}var i=n.handlers;return t in i||(i[t]=[]),i[t].push(e),n.setHandlers(i),n},subscribeOn
ce:function(t,e){o(e);var n,a=this;return this.subscribe.call(this,t,n=function(){a.unsubscribe.call(a,t,n);var o=Array.prototype.slice.call(arguments
);e.apply(a,o)}),this},unsubscribe:function(t,e){o(e);var n=this.handlers[t];if(!n)return this;if("object"==typeof n&amp;&amp;n.length&gt;0){for(var a
=0;a&lt;n.length;a++){var r=e.toString(),i=n[a].toString();r===i&amp;&amp;n.splice(a,1)}this.handlers[t]=n}else delete this.handlers[t];return this},p
ublish:function(t){var e=r(arguments),n=this.handlers,o=n[t]?n[t].length:0;if(o&gt;0)for(var a=0;a&lt;o;a++)n[t][a].apply(this,e);return this},cachePu
bs:function(t){var e=this.pubs||{},n=r(arguments);e[t]=function(){return n}}});t.exports=i},function(t,e){"use strict";function n(){}n.prototype.exten
d=function(){},n.prototype.create=function(){},n.extend=function(t){return this.prototype.extend.call(this,t)},n.prototype.create=function(t){var e=ne
w this;for(var n in t)e[n]=t[n];return e},n.prototype.extend=function(t){var e=function(){};try{"function"!=typeof Object.create&amp;&amp;(Object.crea
te=function(t){function e(){}return e.prototype=t,new e}),e.prototype=Object.create(this.prototype);for(var n in t)e.prototype[n]=t[n];e.prototype.con
structor=e,e.extend=e.prototype.extend,e.create=e.prototype.create}catch(t){console.log(t)}finally{return e}},t.exports=n},function(t,e,n){"use strict
";var o=n(6),a=n(7),r=n(8);e.init=function(){var t=n(8),e=goldlog._$,i=navigator.userAgent;i.match(/AliApp\(([A-Z\-]+)\/([\d\.]+)\)/i)&amp;&amp;(e.is_
ali_app=!0),t.utilPvid.makePVId();var s=n(46);e.spm=s,e.is_WindVane=o.is_WindVane;var u=e.meta_info;e.page_url=location.href,e.page_referrer=n(48).get
Refer(),s.init(goldlog,u,function(){t.initLoad.init_watchGoldlogQueue();var e=n(8).spmException,o=e.is_exception;o||n(87),a.doPubMsg(["aplusReady","co
mplete"]),a.doCachePubs(["aplusReady","complete"])}),goldlog.beforeSendPV(function(t,e){if(e.is_auto&amp;&amp;"1"===u["aplus-manual-pv"])return!1}),go
ldlog.afterSendPV(function(){window.g_SPM&amp;&amp;(g_SPM._current_spm="")}),r.is_auto_pv+""=="true"&amp;&amp;goldlog.sendPV({is_auto:!0}),t.initLoad.
run(),t.beforeUnload.run()}},function(t,e){"use strict";var n=navigator.userAgent,o=/WindVane/i.test(n);e.is_WindVane=o;var a=function(){var t=goldlog
.getMetaInfo("aplus_chnl");return!(!t||!t.isAvailable||"function"!=typeof t.toUT2&amp;&amp;"function"!=typeof t.toUT)&amp;&amp;t};e.isAplusChnl=a,e.ge
tAplusToUT=function(t){var e={},n=a();if("object"==typeof n)e.bridgeName=n.bridgeName||"customBridge",e.isAvailable=n.isAvailable,e.toUT2=n.toUT2||n.t
oUT;else{var r=window.WindVane||{};if(o&amp;&amp;r&amp;&amp;r.isAvailable&amp;&amp;"function"==typeof r.call){var i=t||"toUT";e={bridgeName:"WindVane"
,isAvailable:!0,toUT2:function(t,e,n,o){return r.call("WVTBUserTrack",i,t,e,n,o)}}}}return e}},function(t,e){"use strict";var n=function(){var t=windo
w.goldlog||{},e=t.aplus_pubsub||{},n="function"==typeof e.publish;return n?e:""};e.doPubMsg=function(t){var e=n();e&amp;&amp;e.publish.apply(e,t)},e.d
oCachePubs=function(t){var e=n();e&amp;&amp;"function"==typeof e.cachePubs&amp;&amp;e.cachePubs.apply(e,t)},e.doSubMsg=function(t,e){var o=n();o&amp;&
amp;"function"==typeof o.subscribe&amp;&amp;o.subscribe(t,e)}},function(t,e,n){"use strict";var o=n(9),a=n(10),r=n(11);e.APLUS_ENV="production",e.lver
=a.lver,e.toUtVersion=a.toUtVersion,e.script_name=a.script_name,e.recordTypes=o.recordTypes,e.KEY=o.KEY,e.context=r.context,e.context_prepv=r.context_
prepv,e.aplus_init_plugins=n(18).aplus_init_plugins,e.plugins_pv=n(29).plugins_pv,e.plugins_prepv=n(60).plugins_prepv,e.context_hjlj=n(61),e.plugins_h
jlj=n(63).plugins_hjlj,e.beforeUnload=n(71),e.initLoad=n(73),e.spmException=n(78),e.goldlog_path=n(79),e.is_auto_pv="true",e.utilPvid=n(83),e.disableP
vid="false",e.mustSpmE=!0,e.LS_CNA_KEY="APLUS_CNA"},function(t,e){"use strict";e.recordTypes={hjlj:"COMMON_HJLJ",uhjlj:"DATACLICK_HJLJ",pv:"PV",prepv:
"PREPV"},e.KEY={NAME_STORAGE:{REFERRER:"wm_referrer",REFERRER_PV_ID:"refer_pv_id",LOST_PV_PAGE_DURATION:"lost_pv_page_duration",LOST_PV_PAGE_SPMAB:"lo
st_pv_page_spmab",LOST_PV_PAGE:"lost_pv_page",LOST_PV_PAGE_MSG:"lost_pv_page_msg"}}},function(t,e){"use strict";e.lver="8.3.16",e.toUtVersion="v201804
20",e.script_name="aplus_std"},function(t,e,n){"use strict";e.context=n(12),e.context_prepv=n(17)},function(t,e,n){"use strict";function o(){return{co
mpose:{maxTimeout:5500},etag:{egUrl:"//log.mmstat.com/eg.js",cna:i.getCookie("cna")}}}function a(){return r.assign(new s.initConfig,new o)}var r=n(13)
,i=n(14),s=n(16);t.exports=a},function(t,e){"use strict";function n(t,e){return"function"!=typeof Object.assign?function(t){if(null===t)throw new Type
Error("Cannot convert undefined or null to object");for(var e=Object(t),n=1;n&lt;arguments.length;n++){var o=arguments[n];if(null!==o)for(var a in o)O
bject.prototype.hasOwnProperty.call(o,a)&amp;&amp;(e[a]=o[a])}return e}(t,e):Object.assign({},t,e)}function o(t){return"function"==typeof t}function a
(t){return"[object Array]"===Object.prototype.toString.call(t)}function r(t){return"string"==typeof t}function i(t){return"undefined"==typeof t}functi
on s(t,e){return t.indexOf(e)&gt;-1}var u=window;e.assign=n,e.makeCacheNum=function(){return Math.floor(268435456*Math.random()).toString(16)},e.each=
function(t,e){var n,o=t.length;for(n=0;n&lt;o;n++)e(t[n])},e.isStartWith=function(t,e){return 0===t.indexOf(e)},e.isEndWith=function(t,e){var n=t.leng
th,o=e.length;return n&gt;=o&amp;&amp;t.indexOf(e)==n-o},e.any=function(t,e){var n,o=t.length;for(n=0;n&lt;o;n++)if(e(t[n]))return!0;return!1},e.isFun
ction=o,e.isArray=a,e.isString=r,e.isNumber=function(t){return"number"==typeof t},e.isUnDefined=i,e.isContain=s;var c=function(t){var e,n=t.constructo
r===Array?[]:{};if("object"==typeof t){if(u.JSON&amp;&amp;u.JSON.parse)e=JSON.stringify(t),n=JSON.parse(e);else for(var o in t)n[o]="object"==typeof t
[o]?c(t[o]):t[o];return n}};e.cloneObj=c,e.cloneDeep=c},function(t,e,n){"use strict";function o(t){var e=s.cookie.match(new RegExp("(?:^|;)\\s*"+t+"=(
[^;]+)"));return e?e[1]:""}function a(t,e,n){n||(n={});var a=new Date;return"session"===n.expires||(n.expires&amp;&amp;("number"==typeof n.expires||n.
expires.toUTCString)?("number"==typeof n.expires?a.setTime(a.getTime()+24*n.expires*60*60*1e3):a=n.expires,e+="; expires="+a.toUTCString()):(a.setTime
(a.getTime()+63072e7),e+="; expires="+a.toUTCString())),e+="; path="+(n.path?n.path:"/"),e+="; domain="+n.domain,s.cookie=t+"="+e,o(t)}function r(t,e,
n){try{if(n||(n={}),n.domain)a(t,e,n);else for(var o=c.getDomains(),r=0;r&lt;o.length;)n.domain=o[r],a(t,e,n)?r=o.length:r++}catch(t){}}function i(){v
ar t={};return u.each(p,function(e){t[e]=o(e)}),t.cnaui=/\btanx\.com$/.test(l)?o("cnaui"):"",t}var s=document,u=n(13),c=n(15),l=location.hostname;e.ge
tCookie=o,e.setCookie=r;var p=["tracknick","thw","cna"];e.getData=i,e.getHng=function(){return encodeURIComponent(o("hng")||"")}},function(t,e){"use s
trict";e.getDomains=function(){var t=[];try{for(var e=location.hostname,n=e.split("."),o=2;o&lt;=n.length;)t.push(n.slice(n.length-o).join(".")),o++}c
atch(t){}return t}},function(t,e,n){"use strict";function o(t,e,n){var o=window.goldlog||{},s=o.getMetaInfo("aplus-ifr-pv")+""=="1";return e?r(t)?"yt"
:"m":n&amp;&amp;!s?a.isContain(t,"wrating.com")?"k":i(t)||"y":i(t)||"v"}var a=n(13),r=function(t){for(var e=["youku.com","soku.com","tudou.com","laife
ng.com"],n=0;n&lt;e.length;n++){var o=e[n];if(a.isContain(t,o))return!0}return!1},i=function(t){for(var e=[["scmp.com","sc"],["luxehomes.com.hk","sc"]
,["ays.com.hk","sc"],["cpjobs.com","sc"],["educationpost.com.hk","sc"],["cosmopolitan.com.hk","sc"],["elle.com.hk","sc"],["harpersbazaar.com.hk","sc"]
,["1688.com","6"],["youku.com","yt"],["soku.com","yt"],["tudou.com","yt"],["laifeng.com","yt"]],n=0;n&lt;e.length;n++){var o=e[n];if(a.isContain(t,o[0
]))return o[1]}return""};e.getBeaconSrc=o,e.initConfig=function(){return{compose:{},etag:{egUrl:"//log.mmstat.com/eg.js",cna:"",tag:"",stag:"",lstag:"
-1",lscnastatus:""},can_to_sendpv:{flag:"NO"},userdata:{},what_to_sendpv:{pvdata:{},exparams:{}},what_to_pvhash:{hash:[]},what_to_sendpv_ut:{pvdataToU
t:{}},what_to_sendpv_ut2:{isSuccess:!1,pvdataToUt:{}},when_to_sendpv:{aplusWaiting:""},where_to_sendpv:{url:"//log.mmstat.com/o.gif",urlRule:o},where_
to_sendlog_ut:{aplusToUT:{},toUTName:"toUT"},hjlj:{what_to_hjlj:{logdata:{}},what_to_hjlj_ut:{logdataToUT:{}}},network:{connType:"UNKNOWN"},is_single:
!1}}},function(t,e,n){"use strict";function o(){return{etag:{egUrl:"//log.mmstat.com/eg.js",cna:a.getCookie("cna"),tag:"",stag:""},compose:{},where_to
_prepv:{url:"//log.mmstat.com/v.gif",urlRule:r.getBeaconSrc},userdata:{},what_to_prepv:{logdata:{}},what_to_hjlj_exinfo:{EXPARAMS_FLAG:"EXPARAMS",exin
fo:[],exparams_key_names:["uidaplus","pc_i","pu_i"]},is_single:!1}}var a=n(14),r=n(16);t.exports=o},function(t,e,n){"use strict";e.aplus_init_plugins=
[{name:"etag",enable:!0,path:n(19)}]},function(t,e,n){"use strict";var o=n(14),a=n(20),r=n(27),i=n(23),s=n(28);t.exports=function(){return{init:functi
on(t){this.options=t;var e=this.options.context.etag||{};this.cna=e.cna||o.getCookie("cna"),this.setTag(0),this.setStag(-1),this.setEtag(this.cna||"")
,this.requesting=!1},setTag:function(t){this.tag=t,this.options.context.etag.tag=t},setStag:function(t){this.stag=t,this.options.context.etag.stag=t},
setEtag:function(t){this.etag=t,this.options.context.etag.cna=t,o.getCookie("cna")!==t&amp;&amp;o.setCookie("cna",t)},getUrl:function(){var t=this.opt
ions.context.etag||{},e=a.filterIntUrl(t.egUrl||"//log.mmstat.com/eg.js");try{var n=goldlog.getMetaInfo("aplus-rhost-v"),o=/[[a-z|0-9\.]+[a-z|0-9]/,r=
n.match(o);r&amp;&amp;r[0]&amp;&amp;(e=e.replace(o,r[0]))}catch(t){}return e},run:function(t,e){var n=this;if(n.cna)return void n.setTag(1);var o=null
,a=this.getUrl();if(0===a.indexOf("//")){var u=i.getProtocal();a=u+a}return n.requesting=!0,r.loadScript(a,function(t){if(t&amp;&amp;"error"===t.type&
amp;&amp;n.setStag(-3),n.requesting){n.requesting=!1;var a=s.getGoldlogVal("Etag");a&amp;&amp;n.setEtag(a);var r=s.getGoldlogVal("stag");"undefined"!=
typeof r&amp;&amp;n.setStag(r),clearTimeout(o),e()}}),o=setTimeout(function(){n.requesting=!1,n.setStag(-2),e()},1e3),"pause"}}}},function(t,e,n){"use
 strict";function o(t){t=(t||"").split("#")[0].split("?")[0];var e=t.length,n=function(t){var e,n=t.length,o=0;for(e=0;e&lt;n;e++)o=31*o+t.charCodeAt(
e);return o};return e?n(e+"#"+t.charCodeAt(e-1)):-1}function a(t){for(var e=t.split("&amp;"),n=0,o=e.length,a={};n&lt;o;n++){var r=e[n],i=r.indexOf("=
"),s=r.substring(0,i),u=r.substring(i+1);a[s]=p.tryToDecodeURIComponent(u)}return a}function r(t){if("function"!=typeof t)throw new TypeError(t+" is n
ot a function");return t}function i(t){var e,n,o,a=[],r=t.length;for(o=0;o&lt;r;o++)e=t[o][0],n=t[o][1],a.push(l.isStartWith(e,v)?n:e+"="+encodeURICom
ponent(n));return a.join("&amp;")}function s(t){var e,n,o,a={},r=t.length;for(o=0;o&lt;r;o++)e=t[o][0],n=t[o][1],a[e]=n;return a}function u(t,e){var n
,o,a,r=[];for(n in t)t.hasOwnProperty(n)&amp;&amp;(o=""+t[n],a=n+"="+encodeURIComponent(o),e?r.push(a):r.push(l.isStartWith(n,v)?o:a));return r.join("
&amp;")}function c(t,e){var n=t.indexOf("?")==-1?"?":"&amp;",o=e?l.isArray(e)?i(e):u(e):"";return o?t+n+o:t}var l=n(13),p=n(21),g=n(23),f=parent!==sel
f;e.is_in_iframe=f,e.makeCacheNum=l.makeCacheNum,e.isStartWith=l.isStartWith,e.isEndWith=l.isEndWith,e.any=l.any,e.each=l.each,e.assign=l.assign,e.isF
unction=l.isFunction,e.isArray=l.isArray,e.isString=l.isString,e.isNumber=l.isNumber,e.isUnDefined=l.isUnDefined,e.isContain=l.isContain,e.sleep=n(24)
.sleep,e.makeChkSum=o,e.tryToDecodeURIComponent=p.tryToDecodeURIComponent,e.nodeListToArray=p.nodeListToArray,e.parseSemicolonContent=p.parseSemicolon
Content,e.param2obj=a;var d=n(25),h=function(t){return/^(\/\/){0,1}(\w+\.){1,}\w+((\/\w+){1,})?$/.test(t)};e.hostValidity=h;var _=function(t,e){var n=
/^(\/\/){0,1}(\w+\.){1,}\w+\/\w+\.gif$/.test(t),o=h(t),a="";return n?a="isGifPath":o&amp;&amp;(a="isHostPath"),a||d.logger({msg:e+": "+t+' is invalid,
 suggestion: "xxx.mmstat.com"'}),a},m=function(t){return!/^\/\/gj\.mmstat/.test(t)&amp;&amp;goldlog.isInternational()&amp;&amp;(t=t.replace(/^\/\/\w+\
.mmstat/,"//gj.mmstat")),t};e.filterIntUrl=m,e.getPvUrl=function(t){t||(t={});var e,n,o=t.metaValue&amp;&amp;_(t.metaValue,t.metaName),a="";"isGifPath
"===o?(e=/^\/\//.test(t.metaValue)?"":"//",a=e+t.metaValue):"isHostPath"===o&amp;&amp;(e=/^\/\//.test(t.metaValue)?"":"//",n=/\/$/.test(t.metaValue)?"
":"/",a=e+t.metaValue+n+t.gifPath);var r;return a?r=a:(e=0===t.gifPath.indexOf("/")?t.gifPath:"/"+t.gifPath,r=t.url&amp;&amp;t.url.replace(/\/\w+\.gif
/,e)),r},e.indexof=n(26).indexof,e.callable=r;var v="::-plain-::";e.mkPlainKey=function(){return v+Math.random()},e.s_plain_obj=v,e.mkPlainKeyForExpar
ams=function(t){var e=t||v;return e+"exparams"},e.rndInt32=function(){return Math.round(2147483647*Math.random())},e.arr2param=i,e.arr2obj=s,e.obj2par
am=u,e.makeUrl=c,e.ifAdd=function(t,e){var n,o,a,r,i=e.length;for(n=0;n&lt;i;n++)o=e[n],a=o[0],r=o[1],r&amp;&amp;t.push([a,r])},e.isStartWithProtocol=
g.isStartWithProtocol,e.param2arr=function(t){for(var e,n=t.split("&amp;"),o=0,a=n.length,r=[];o&lt;a;o++)e=n[o].split("="),r.push([e.shift(),e.join("
=")]);return r}},function(t,e,n){"use strict";function o(t,e){var n=e||"";if(t)try{n=decodeURIComponent(t)}catch(t){}return n}var a=n(22);e.tryToDecod
eURIComponent=o,e.parseSemicolonContent=function(t,e,n){e=e||{};var r,i,s=t.split(";"),u=s.length;for(r=0;r&lt;u;r++){i=s[r].split("=");var c=a.trim(i
.slice(1).join("="));e[a.trim(i[0])||""]=n?c:o(c)}return e},e.nodeListToArray=function(t){var e,n;try{return e=[].slice.call(t)}catch(a){e=[],n=t.leng
th;for(var o=0;o&lt;n;o++)e.push(t[o]);return e}},e.nodeListToArray=function(t){var e,n;try{return e=[].slice.call(t)}catch(a){e=[],n=t.length;for(var
 o=0;o&lt;n;o++)e.push(t[o]);return e}};var r={set:function(t,e){try{return localStorage.setItem(t,e),!0}catch(t){return!1}},get:function(t){return lo
calStorage.getItem(t)},test:function(){var t="grey_test_key";try{return localStorage.setItem(t,1),localStorage.removeItem(t),!0}catch(t){return!1}},re
move:function(t){localStorage.removeItem(t)}};e.store=r,e.getLsCna=function(t,e){var n="",o=r.get(t);if(o){var a=o.split("_")||[];n=e?a.length&gt;1&am
p;&amp;e===a[0]?a[1]:"":a.length&gt;1?a[1]:""}return decodeURIComponent(n)},e.setLsCna=function(t,e,n){n&amp;&amp;r.set&amp;&amp;r.test()&amp;&amp;r.s
et(t,e+"_"+encodeURIComponent(n))},e.getUrl=function(t){var e=t||"//log.mmstat.com/eg.js";try{var n=goldlog.getMetaInfo("aplus-rhost-v"),o=/[[a-z|0-9\
.]+[a-z|0-9]/,a=n.match(o);a&amp;&amp;a[0]&amp;&amp;(e=e.replace(o,a[0]))}catch(t){}return e}},function(t,e){"use strict";function n(t){return"string"
==typeof t?t.replace(/^\s+|\s+$/g,""):""}e.trim=n},function(t,e,n){"use strict";var o=n(13),a=function(){var t=location.protocol;return"http:"!==t&amp
;&amp;"https:"!==t&amp;&amp;(t="https:"),t};e.getProtocal=a,e.isStartWithProtocol=function(t){for(var e=["javascript:","tel:","sms:","mailto:","tmall:
//","#"],n=0,a=e.length;n&lt;a;n++)if(o.isStartWith(t,e[n]))return!0;return!1}},function(t,e){"use strict";e.sleep=function(t,e){return setTimeout(fun
ction(){e()},t)}},function(t,e){"use strict";var n=function(){var t=!1;return"boolean"==typeof goldlog.aplusDebug&amp;&amp;(t=goldlog.aplusDebug),t};e
.isDebugAplus=n;var o=function(t){t||(t={});var e=t.level||"warn";window.console&amp;&amp;window.console[e]&amp;&amp;window.console[e](t.msg)};e.logge
r=o},function(t,e){"use strict";e.indexof=function(t,e){var n=-1;try{n=t.indexOf(e)}catch(a){for(var o=0;o&lt;t.length;o++)t[o]===e&amp;&amp;(n=o)}fin
ally{return n}}},function(t,e,n){"use strict";function o(t,e){return t&amp;&amp;t.getAttribute?t.getAttribute(e)||"":""}function a(t,e,n){if(t&amp;&am
p;t.setAttribute)try{t.setAttribute(e,n)}catch(t){}}function r(t,e){if(t&amp;&amp;t.removeAttribute)try{t.removeAttribute(e)}catch(n){a(t,e,"")}}funct
ion i(t,e,n){var o="script",a=g.createElement(o);a.type="text/javascript",a.async=!0;var r="https:"==location.protocol?e||t:t;0===r.indexOf("//")&amp;
&amp;(r=u.getProtocal()+r),a.src=r,n&amp;&amp;(a.id=n);var i=g.getElementsByTagName(o)[0];s=s||g.getElementsByTagName("head")[0],i?i.parentNode.insert
Before(a,i):s&amp;&amp;s.appendChild(a)}var s,u=n(23),c=n(22),l=n(13),p=n(25),g=document;e.tryToGetAttribute=o,e.tryToSetAttribute=a,e.tryToRemoveAttr
ibute=r,e.addScript=i,e.loadScript=function(t,e){function n(t){o.onreadystatechange=o.onload=o.onerror=null,o=null,e(t)}var o=g.createElement("script"
);if(s=s||g.getElementsByTagName("head")[0],o.async=!0,"onload"in o)o.onload=n;else{var a=function(){/loaded|complete/.test(o.readyState)&amp;&amp;n()
};o.onreadystatechange=a,a()}o.onerror=function(t){n(t)},o.src=t,s.appendChild(o)},e.isTouch=function(){return"ontouchend"in document.createElement("d
iv")},e.tryToGetHref=function(t){var e;try{e=c.trim(t.getAttribute("href",2))}catch(t){}return e||""};var f=function(){var t=goldlog&amp;&amp;goldlog.
_$?goldlog._$:{},e=t.meta_info||{};return e["aplus-exparams"]||""};e.getExParamsFromMeta=f,e.getExParams=function(t){var e=g.getElementById("beacon-ap
lus")||g.getElementById("tb-beacon-aplus"),n=o(e,"exparams"),a=d(n,f(),t)||"";return a&amp;&amp;a.replace(/&amp;amp;/g,"&amp;").replace(/\buserid=/,"u
idaplus=")};var d=function(t,e,n){var o="aplus&amp;sidx=aplusSidex",a=t||o;try{if(e){var r=n.param2obj(e),i=["aplus","cna","spm-cnt","spm-url","spm-pr
e","logtype","pre","uidaplus","asid","sidx","trid","gokey"];l.each(i,function(t){r.hasOwnProperty(t)&amp;&amp;(p.logger({msg:"Can not inject keywords:
 "+t}),delete r[t])}),delete r[""];var s="";if(t){var u=t.match(/aplus&amp;/).index,c=u&gt;0?n.param2obj(t.substring(0,u)):{};delete c[""],s=n.obj2par
am(l.assign(c,r))+"&amp;"+t.substring(u,t.length)}else s=n.obj2param(r)+"&amp;"+o;return s}return a}catch(t){return a}};e.mergeExparams=d},function(t,
e){"use strict";var n=function(t){var e;try{window.goldlog||(window.goldlog={}),e=window.goldlog[t]}catch(t){e=""}finally{return e}};e.getGoldlogVal=n
;var o=function(t,e){var n=!1;try{window.goldlog||(window.goldlog={}),t&amp;&amp;(window.goldlog[t]=e,n=!0)}catch(t){n=!1}finally{return n}};e.setGold
logVal=o,e.getClientInfo=function(){return n("_aplus_client")||{}}},function(t,e,n){"use strict";e.plugins_pv=[{name:"etag",enable:!0,path:n(30)},{nam
e:"etag_sync",enable:!0,path:n(32)},{name:"when_to_sendpv",enable:!0,path:n(33)},{name:"where_to_sendlog_ut",enable:!0,path:n(36)},{name:"is_single",e
nable:!0,path:n(37)},{name:"what_to_pvhash",enable:!0,path:n(40)},{name:"what_to_sendpv",enable:!0,path:n(41)},{name:"what_to_sendpv_userdata",enable:
!0,path:n(45),deps:["what_to_sendpv"]},{name:"what_to_sendpv_etag",enable:!0,path:n(50),deps:["etag","what_to_sendpv"]},{name:"what_to_sendpv_ut",enab
le:!0,path:n(51),deps:["where_to_sendlog_ut","is_single"]},{name:"what_to_pv_slog",enable:!0,path:n(52),deps:["what_to_sendpv"]},{name:"can_to_sendpv"
,enable:!0,path:n(53)},{name:"where_to_sendpv",enable:!0,path:n(54),deps:["is_single"]},{name:"do_sendpv",enable:!0,path:n(55),deps:["is_single","what
_to_sendpv","where_to_sendpv"]},{name:"do_sendpv_ut",enable:!0,path:n(56),deps:["what_to_sendpv_ut","where_to_sendlog_ut"]},{name:"cookiemapping",enab
le:!0,path:n(57),deps:["do_sendpv"]},{name:"after_pv",enable:!0,path:n(59)}]},function(t,e,n){"use strict";var o=n(14),a=n(27),r=n(21),i=n(31),s=n(23)
,u=n(28),c=n(8);t.exports=function(){return{init:function(t){this.options=t;var e=this.options.context.etag||{};this.cna=e.cna||o.getCookie("cna"),thi
s.setTag(0),this.setStag(-1),this.setLsTag("-1"),this.setEtag(this.cna||""),this.requesting=!1,this.today=i.getFormatDate()},setLsTag:function(t){this
.lstag=t,this.options.context.etag.lstag=t},setTag:function(t){this.tag=t,this.options.context.etag.tag=t},setStag:function(t){this.stag=t,this.option
s.context.etag.stag=t},setEtag:function(t){this.etag=t,this.options.context.etag.cna=t,o.getCookie("cna")!==t&amp;&amp;o.setCookie("cna",t)},setLscnaS
tatus:function(t){this.options.context.etag.lscnastatus=t},getUrl:function(){var t=this.options.context.etag||{};return r.getUrl(t.egUrl||"//log.mmsta
t.com/eg.js")},run:function(t,e){var n=this;if(n.cna)return void n.setTag(1);var o=null,i=this.getUrl();if(0===i.indexOf("//")){var l=s.getProtocal();
i=l+i}n.requesting=!0;var p=function(){setTimeout(function(){e()},20),clearTimeout(o)};return a.loadScript(i,function(t){var e,o;if(t&amp;&amp;"error"
===t.type?n.setStag(-3):(e=u.getGoldlogVal("Etag"),e&amp;&amp;n.setEtag(e),o=u.getGoldlogVal("stag"),"undefined"!=typeof o&amp;&amp;n.setStag(o)),n.re
questing){if(2===o||4===o){var a=r.getLsCna(c.LS_CNA_KEY);a?(n.setLsTag(1),n.setEtag(a)):(n.setLsTag(0),r.setLsCna(c.LS_CNA_KEY,n.today,e))}p()}}),o=s
etTimeout(function(){n.requesting=!1,n.setStag(-2),e()},1500),2e3}}}},function(t,e){"use strict";function n(t,e,n){var o=""+Math.abs(t),a=e-o.length,r
=t&gt;=0;return(r?n?"+":"":"-")+Math.pow(10,Math.max(0,a)).toString().substr(1)+o}e.getFormatDate=function(t){var e=new Date;try{return[e.getFullYear(
),n(e.getMonth()+1,2,0),n(e.getDate(),2,0)].join(t||"")}catch(t){return""}}},function(t,e,n){"use strict";var o=n(21),a=n(27),r=n(8),i=n(31),s=o.store
||{};t.exports=function(){return{init:function(t){this.options=t,this.today=i.getFormatDate()},getUrl:function(){var t=this.options.context.etag||{};r
eturn o.getUrl(t.egUrl||"//log.mmstat.com/eg.js")},run:function(){var t=this;if(s.test()){var e=o.getLsCna(r.LS_CNA_KEY,this.today);e||setTimeout(func
tion(){a.loadScript(t.getUrl(),function(e){e&amp;&amp;"error"!==e.type&amp;&amp;o.setLsCna(r.LS_CNA_KEY,t.today,goldlog.Etag)})},1e3)}}}}},function(t,
e,n){"use strict";var o=n(28),a=n(24),r=n(34);t.exports=function(){return{init:function(t){this.options=t},getMetaInfo:function(){var t=o.getGoldlogVa
l("_$")||{},e=t.meta_info||r.getInfo();return e},getAplusWaiting:function(){var t=this.getMetaInfo()||{};return t["aplus-waiting"]},run:function(t,e){
var n=this.options.config||{},o=this.getAplusWaiting();if(o&amp;&amp;n.is_auto)switch(o=this.getAplusWaiting()+"",this.options.context.when_to_sendpv=
{aplusWaiting:o},o){case"MAN":return"done";case"1":return this.options.context.when_to_sendpv.isWait=!0,a.sleep(6e3,function(){e()}),6e3;default:var r
=1*o;if(r+""!="NaN")return this.options.context.when_to_sendpv.isWait=!0,a.sleep(r,function(){e()}),r}}}}},function(t,e,n){"use strict";function o(t){
var e,n,o,a=t.length,r={};for(g._microscope_data=r,e=0;e&lt;a;e++)n=t[e],"microscope-data"==l.tryToGetAttribute(n,"name")&amp;&amp;(o=l.tryToGetAttrib
ute(n,"content"),u.parseSemicolonContent(o,r),g.is_head_has_meta_microscope_data=!0);g._microscope_data_params=u.obj2param(r),g.ms_data_page_id=r.page
Id,g.ms_data_shop_id=r.shopId,g.ms_data_instance_id=r.siteInstanceId,g.ms_data_siteCategoryId=r.siteCategory,g.ms_prototype_id=r.prototypeId,g.site_in
stance_id_or_shop_id=g.ms_data_instance_id||g.ms_data_shop_id,g._atp_beacon_data={},g._atp_beacon_data_params=""}function a(t){var e,n=function(){var
e;return document.querySelector&amp;&amp;(e=document.querySelector("meta[name=data-spm]")),c.each(t,function(t){"data-spm"===l.tryToGetAttribute(t,"na
me")&amp;&amp;(e=t)}),e},o=n();return o&amp;&amp;(e=l.tryToGetAttribute(o,"data-spm-protocol")),e}function r(t){var e=t.isonepage||"-1",n=e.split("|")
,o=n[0],a=n[1]?n[1]:"";t.isonepage_data={isonepage:o,urlpagename:a}}function i(){var t=p.getMetaTags();o(t),c.each(t,function(t){var e=l.tryToGetAttri
bute(t,"name");/^aplus/.test(e)&amp;&amp;(g[e]=p.getMetaCnt(e))}),c.each(f,function(t){g[t]=p.getMetaCnt(t)}),g.spm_protocol=a(t);var e,n,i=["aplus-ra
te-ahot"],s=i.length;for(e=0;e&lt;s;e++)n=i[e],g[n]=parseFloat(g[n]);return r(g),d=g||{},g}function s(){return d||i()}var u=n(20),c=n(13),l=n(27),p=n(
35),g={},f=["ahot-aplus","isonepage","spm-id","data-spm","microscope-data"],d={};e.setMetaInfo=function(t,e){return d||(d={}),d[t]=e,!0},e.getMetaInfo
=function(t){return d||(d={}),d[t]||""},e.getInfo=i,e.qGet=s},function(t,e,n){"use strict";function o(t){return i=i||document.getElementsByTagName("he
ad")[0],s&amp;&amp;!t?s:i?s=i.getElementsByTagName("meta"):[]}function a(t){var e,n,a,r=o(),i=r.length;for(e=0;e&lt;i;e++)n=r[e],u.tryToGetAttribute(n
,"name")===t&amp;&amp;(a=u.tryToGetAttribute(n,"content"));return a||""}function r(t){var e={isonepage:"-1",urlpagename:""},n=t.qGet();if(n&amp;&amp;n
.hasOwnProperty("isonepage_data"))e.isonepage=n.isonepage_data.isonepage,e.urlpagename=n.isonepage_data.urlpagename;else{var o=a("isonepage")||"-1",r=
o.split("|");e.isonepage=r[0],e.urlpagename=r[1]?r[1]:""}return e}var i,s,u=n(27);e.getMetaTags=o,e.getMetaCnt=a,e.getOnePageInfo=r},function(t,e,n){"
use strict";var o=n(6);t.exports=function(){return{init:function(t){this.options=t},getAplusToUT:function(){return{toUT2:o.getAplusToUT("toUT2"),toUT:
o.getAplusToUT("toUT")}},run:function(){var t=this.getAplusToUT();this.options.context.where_to_sendlog_ut.aplusToUT=t}}}},function(t,e,n){"use strict
";var o=n(28),a=n(38),r=n(8);t.exports=function(){var t=o.getGoldlogVal("isUT4Aplus");return{init:function(t){this.options=t},isBoth:function(t){retur
n"1"===t.meta_info["aplus-both-request"]},isSingle_pv:function(){var e=o.getGoldlogVal("_$")||{};return!(!t&amp;&amp;!e.is_WindVane||!a.isSingleUaVers
ion()||this.isBoth(e))},isSingle_hjlj:function(e){var n=o.getGoldlogVal("_$")||{};return!(!t&amp;&amp;!n.is_WindVane||!a.isSingleSendLog(e)||this.isBo
th(n))},isSingle_uhjlj:function(e){var n=o.getGoldlogVal("_$")||{};return(!e||!/^\/aplus\.99\.(\d)+$/.test(e.logkey))&amp;&amp;!(!((t||n.is_WindVane)&
amp;&amp;e&amp;&amp;e.logkey&amp;&amp;a.isSingleUaVersion())||this.isBoth(n))},run:function(){var t=this.options.context||{},e=this.options.config||{}
,n=t.where_to_sendlog_ut.aplusToUT||{},o=n.toUT||{},a=n.toUT2||{},i=!(!o.isAvailable&amp;&amp;!a.isAvailable),s=t.userdata||{},u=!!t.is_single;switch(
e.recordType){case r.recordTypes.uhjlj:u=this.isSingle_uhjlj(s);break;case r.recordTypes.hjlj:u=this.isSingle_hjlj(s);break;case r.recordTypes.pv:u=th
is.isSingle_pv(s);break;default:u=this.isSingle_pv(s)}this.options.context.is_single=i&amp;&amp;u}}}},function(t,e,n){"use strict";var o=n(39),a=funct
ion(t){var e=t.logkey.toLowerCase();0===e.indexOf("/")&amp;&amp;(e=e.substr(1));var n=t.gmkey.toUpperCase();switch(n){case"EXP":return"2201";case"CLK"
:return"2101";case"SLD":return"19999";case"OTHER":default:return"19999"}},r=function(){var t=!1;return t||goldlog.isUT4Aplus||o.webviewIsAbove({versio
n_ios_tb:[5,11,7],version_ios_tm:[5,24,1],version_android_tb:[5,11,7],version_android_tm:[5,24,1]})};e.isSingleUaVersion=r,e.isSingleSendLog=function(
t){return(!t||!/^\/fsp\.1\.1$/.test(t.logkey))&amp;&amp;!!(t&amp;&amp;t.logkey&amp;&amp;r())},e.getFunctypeValue=function(t){return e.isSingleSendLog(
t)?a(t):"2101"},e.getFunctypeValue2=function(t){return a(t)}},function(t,e){"use strict";var n=function(t){var e=[0,0,0];try{if(t){var n=t[1],o=n.spli
t(".");if(o.length&gt;2)for(var a=0;a&lt;o.length;)e[a]=parseInt(o[a]),a++}}catch(t){e=[0,0,0]}finally{return e}};e.parseVersion=n;var o=function(t,e)
{var n=!1;try{var o=t[0]&gt;e[0],a=t[1]&gt;e[1],r=t[2]&gt;e[2],i=t[0]===e[0],s=t[1]===e[1],u=t[2]===e[2];n=!!o||(!(!i||!a)||(!!(i&amp;&amp;s&amp;&amp;
r)||!!(i&amp;&amp;s&amp;&amp;u)))}catch(t){n=!1}finally{return n}};e.isAboveVersion=o,e.webviewIsAbove=function(t,e){var a=!1;try{e||(e=navigator.user
Agent);var r=e.match(/AliApp\(TB\/(\d+[._]\d+[._]\d+)/i),i=n(r),s=e.match(/AliApp\(TM\/(\d+[._]\d+[._]\d+)/i),u=n(s),c=/iPhone|iPad|iPod|ios/i.test(e)
,l=/android/i.test(e);c?r&amp;&amp;i?a=o(i,t.version_ios_tb):s&amp;&amp;u&amp;&amp;(a=o(u,t.version_ios_tm)):l&amp;&amp;(r&amp;&amp;i?a=o(i,t.version_
android_tb):s&amp;&amp;u&amp;&amp;(a=o(u,t.version_android_tm)))}catch(t){a=!1}return a}},function(t,e,n){"use strict";var o=n(28);t.exports=function(
){return{init:function(t){this.options=t},run:function(){var t=this.options.context.what_to_pvhash||{},e=o.getGoldlogVal("_$")||{},n=e.meta_info||{},a
=n["aplus-pvhash"]||"",r=[];"1"===a&amp;&amp;(r=["_aqx_uri",encodeURIComponent(location.href)]),t.hash=r,this.options.context.what_to_pvhash=t}}}},fun
ction(t,e,n){"use strict";var o=n(20),a=n(13),r=n(27),i=n(28),s=n(14),u=n(42),c=n(43),l=n(44);t.exports=function(){return a.assign(l,{init:function(t)
{this.options=t,this.cookie_data||(this.cookie_data=s.getData()),this.client_info||(this.client_info=i.getClientInfo()||{});var e=location.hash;e&amp;
&amp;0===e.indexOf("#")&amp;&amp;(e=e.substr(1)),this.loc_hash=e},getExParams:function(){var t=window,e=document,n=[],i=parent!==t.self,s=e.getElement
ById("beacon-aplus")||e.getElementById("tb-beacon-aplus"),c=r.tryToGetAttribute(s,"exparams"),l=r.mergeExparams(c,r.getExParamsFromMeta(),o)||"";l=l.r
eplace(/&amp;amp;/g,"&amp;");var p,g,f=["taobao.com","tmall.com","etao.com","hitao.com","taohua.com","juhuasuan.com","alimama.com"];if(i){for(g=f.leng
th,p=0;p&lt;g;p++)if(o.isContain(location.hostname,f[p]))return n.push([o.mkPlainKeyForExparams(),l]),n;l=l.replace(/\buserid=\w*&amp;?/,"")}l=l.repla
ce(/\buserid=/,"uidaplus="),l&amp;&amp;n.push([o.mkPlainKeyForExparams(),l]);var d=a.makeCacheNum();return u.updateKey(n,"cache",d),n},getExtra:functi
on(){var t=[],e=i.getGoldlogVal("_$")||{},n=e.meta_info||{},a=this.cookie_data||{},r=this.getClientInfo(!0)||[];return o.ifAdd(t,r),o.ifAdd(t,[["thw",
a.thw],["bucket_id",c.getBucketId(n)],["urlokey",this.loc_hash],["wm_instanceid",n.ms_data_instance_id]]),t}})}},function(t,e){"use strict";function n
(t,e,n){r(t,"spm-cnt",function(t){var o=t.split(".");return o[0]=goldlog.spm_ab[0],o[1]=goldlog.spm_ab[1],e?o[1]=o[1].split("/")[0]+"/"+e:o[1]=o[1].sp
lit("/")[0],n&amp;&amp;(o[4]=n),o.join(".")})}function o(t,e){var n=window.g_SPM&amp;&amp;g_SPM._current_spm;n&amp;&amp;r(t,"spm-url",function(){retur
n[n.a,n.b,n.c,n.d].join(".")+(e?"."+e:"")},"spm-cnt")}function a(t,e){var n,o,a,r=-1;for(n=0,o=t.length;n&lt;o;n++)if(a=t[n],a[0]===e){r=n;break}r&gt;
=0&amp;&amp;t.splice(r,1)}function r(t,e,n,o){var a,r,i=t.length,s=-1,u="function"==typeof n;for(a=0;a&lt;i;a++){if(r=t[a],r[0]===e)return void(u?r[1]
=n(r[1]):r[1]=n);o&amp;&amp;r[0]===o&amp;&amp;(s=a)}o&amp;&amp;(u&amp;&amp;(n=n()),s&gt;-1?t.splice(s,0,[e,n]):t.push([e,n]))}t.exports={updateSPMCnt:
n,updateSPMUrl:o,updateKey:r,removeKey:a}},function(t,e,n){"use strict";function o(t,e){var n,o=2146271213;for(n=0;n&lt;t.length;n++)o=(o&lt;&lt;5)+o+
t.charCodeAt(n);return(65535&amp;o)%e}function a(t){var e,n=r.getCookie("t");return"3"!=t.ms_prototype_id&amp;&amp;"5"!=t.ms_prototype_id||(e=n?o(n,20
):""),e}var r=n(14);e.getBucketId=a},function(t,e,n){"use strict";var o=n(20),a=n(13),r=n(28),i=n(6),s=n(14),u=n(8);t.exports={init:function(t){this.o
ptions=t,this.cookie_data||(this.cookie_data=s.getData())},getBasicParams:function(){var t=document,e=r.getGoldlogVal("_$")||{},n=e.spm||{},i=e.meta_i
nfo||{},u=i["aplus-ifr-pv"]+""=="1",c=o.is_in_iframe&amp;&amp;!u?0:1,l=[["logtype",c],[o.mkPlainKey(),"title="+escape(t.title)],["pre",e.page_referrer
],["cache",a.makeCacheNum()],["scr",screen.width+"x"+screen.height]],p=this.cookie_data||{},g=this.options.context||{},f=g.etag||{},d=f.cna||p.cna||s.
getCookie("cna");d&amp;&amp;l.push([o.mkPlainKey(),"cna="+d]),p.tracknick&amp;&amp;l.push([o.mkPlainKey(),"nick="+p.tracknick]);var h=n.spm_url||"";re
turn o.ifAdd(l,[["wm_pageid",i.ms_data_page_id],["wm_prototypeid",i.ms_prototype_id],["wm_sid",i.ms_data_shop_id],["spm-url",h],["spm-pre",n.spm_pre],
["spm-cnt",n.spm_cnt],["cnaui",p.cnaui]]),l},getExParams:function(){return[]},getExtra:function(){return[]},getClientInfo:function(t){var e=[],n=r.get
GoldlogVal("_$")||{},a=this.client_info||{},s=a.ua_info||{};if(t||!i.is_WindVane&amp;&amp;!i.isAplusChnl()){for(var c,l=[],p=["p","o","b","s","w","wx"
,"ism"],g=0;c=p[g++];)s[c]&amp;&amp;l.push([c,s[c]]);o.ifAdd(e,l)}o.ifAdd(e,[["lver",goldlog.lver||u.lver],["jsver",n.script_name||u.script_name],["pv
er",goldlog.aplus_cplugin_ver]]);var f=this.options.config||{},d=f.is_auto;return d||o.ifAdd(e,[["mansndlog",1]]),e},processLodashDollar:function(){
var t=r.getGoldlogVal("_$")||{};t.page_url!==location.href&amp;&amp;(t.page_referrer=t.page_url,t.page_url=location.href),r.setGoldlogVal("_$",t)},get
LsParams:function(){var t=r.getGoldlogVal("_$")||{},e=[];return t.lsparams&amp;&amp;t.lsparams.spm_id&amp;&amp;(e.push(["lsparams",t.lsparams.spm_id])
,e.push(["lsparams_pre",t.lsparams.current_url])),e},run:function(){var t=this.getBasicParams()||[],e=this.getExParams()||[],n=this.getExtra()||[];thi
s.processLodashDollar();var o=this.getLsParams()||[],a=[].concat(t,e,n,o);this.options.context.what_to_sendpv.pvdata=a,this.options.context.what_to_se
ndpv.exparams=e}}},function(t,e,n){"use strict";var o=n(20),a=n(28),r=n(42),i=n(14),s=n(46);t.exports=function(){return{init:function(t){this.options=
t},getPageId:function(){var t=this.options.config||{},e=this.options.context||{},n=e.userdata||{};return t.page_id||t.pageid||t.pageId||n.page_id},get
Userdata:function(){var t=a.getGoldlogVal("_$")||{},e=t.spm||{},n=this.options.context||{},r=n.userdata||{},u=this.options.config||{},c=[];if(u&amp;&a
mp;!u.is_auto){u.gokey&amp;&amp;c.push([o.mkPlainKey(),u.gokey]);var l=e.data.b;if(l){var p=this.getPageId();l=p?l.split("/")[0]+"/"+p:l.split("/")[0]
,s.setB(l);var g=e.spm_cnt.split(".");g&amp;&amp;g.length&gt;2&amp;&amp;(g[1]=l,e.spm_cnt=g.join("."))}}var f=function(t){if("object"==typeof t)for(va
r e in t)"object"!=typeof t[e]&amp;&amp;"function"!=typeof t[e]&amp;&amp;c.push([e,t[e]])};f(goldlog.getMetaInfo("aplus-cpvdata")),f(r);var d=i.getCoo
kie("workno")||i.getCookie("emplId");d&amp;&amp;c.push(["workno",d]);var h=i.getHng();return h&amp;&amp;c.push(["_hng",i.getHng()]),c},processLodashDo
llar:function(){var t=this.options.config||{},e=a.getGoldlogVal("_$")||{};t&amp;&amp;t.referrer&amp;&amp;(e.page_referrer=t.referrer),a.setGoldlogVal(
"_$",e)},updatePre:function(t){var e=a.getGoldlogVal("_$")||{};return e.page_referrer&amp;&amp;r.updateKey(t,"pre",e.page_referrer),t},run:function(){
var t=this.options.context.what_to_sendpv.pvdata,e=this.getUserdata();this.processLodashDollar();var n=t,o=this.options.context.what_to_pvhash.hash;o&
amp;&amp;o.length&gt;0&amp;&amp;n.push(o),n=n.concat(e),n=this.updatePre(n);var a=this.getPageId();a&amp;&amp;r.updateSPMCnt(n,a),this.options.context
.what_to_sendpv.pvdata=n,this.options.context.userdata=e}}}},function(t,e,n){"use strict";function o(){if(!s.data.a||!s.data.b){var t=r._SPM_a,e=r._SP
M_b;if(t&amp;&amp;e)return t=t.replace(/^{(\w+\/)}$/g,"$1"),e=e.replace(/^{(\w+\/)}$/g,"$1"),s.is_wh_in_page=!0,void c.setAB(t,e);var n=goldlog._$.met
a_info;t=n["data-spm"]||n["spm-id"]||"0";var o=t.split(".");o.length&gt;1&amp;&amp;(t=o[0],e=o[1]),c.setA(t),e&amp;&amp;c.setB(e);var a=i.getElementsB
yTagName("body");a=a&amp;&amp;a.length?a[0]:null,a&amp;&amp;(e=l.tryToGetAttribute(a,"data-spm"),e?c.setB(e):1===o.length&amp;&amp;c.setAB("0","0"))}}
function a(){var t=s.data.a,e=s.data.b;t&amp;&amp;e&amp;&amp;(goldlog.spm_ab=[t,e])}var r=window,i=document,s={},u={};s.data=u;var c={},l=n(27),p=n(47
),g=location.href,f=n(48).getRefer(),d=n(8);c.setA=function(t){s.data.a=t,a()},c.setB=function(t){s.data.b=t,a()},c.setAB=function(t,e){s.data.a=t,s.d
ata.b=e,a()};var h=p.getSPMFromUrl,_=function(){var t=d.utilPvid.makePVId();return d.mustSpmE?t||goldlog.pvid||"":t||""},m=function(t,e){var n=t.goldl
og||window.goldlog||{},a=n.meta_info||{};s.meta_protocol=a.spm_protocol;var r,i=n.spm_ab||[],u=i[0]||"0",c=i[1]||"0";"0"===u&amp;&amp;"0"===c&amp;&amp
;(o(),u=s.data.a||"0",c=s.data.b||"0"),r=[s.data.a,s.data.b].join("."),s.spm_cnt=(r||"0.0")+".0.0";var l=t.send_pv_count&gt;0?_():n.pvid;l&amp;&amp;(s
.spm_cnt+="."+l),n._$.spm=s,"function"==typeof e&amp;&amp;e(l)};c.spaInit=function(t,e,n,o){var a="function"==typeof o?o:function(){},r=s.spm_url,i=wi
ndow.g_SPM||{},u=t._$||{},c=u.send_pv_count;m({goldlog:t,meta_info:e,send_pv_count:c},function(t){s.spm_cnt=s.data.a+"."+s.data.b+".0.0"+(t?"."+t:"");
var n=e["aplus-spm-fixed"];if("1"!==n){s.spm_pre=h(f),s.spm_url=h(location.href);var o=i._current_spm||{};o&amp;&amp;o.a&amp;&amp;"0"!==o.a&amp;&amp;o
.b&amp;&amp;"0"!==o.b&amp;&amp;(s.spm_url=[o.a,o.b,o.c,o.d,o.e].join("."),s.spm_pre=r)}a()})},c.init=function(t,e,n){s.spm_url=h(g),s.spm_pre=h(f),m({
goldlog:t,meta_info:e},function(){"function"==typeof n&amp;&amp;n()})},c.resetSpmCntPvid=function(){var t=goldlog.spm_ab;if(t&amp;&amp;2===t.length){v
ar e=t.join(".")+".0.0",n=_();n&amp;&amp;(e=e+"."+n),s.spm_cnt=e,s.spm_url=e,goldlog._$.spm=s}},t.exports=c},function(t,e){"use strict";function n(t,e
){if(!t||!e)return"";var n,o="";try{var a=new RegExp(t+"=([^&amp;|#|?|/]+)");if("spm"===t||"scm"===t){var r=new RegExp("\\?.*"+t+"=([\\w\\.\\-\\*/]+)"
),i=e.match(a),s=e.match(r),u=i&amp;&amp;2===i.length?i[1]:"",c=s&amp;&amp;2===s.length?s[1]:"";o=u&gt;c?u:c,o=decodeURIComponent(o)}else n=e.match(a)
,o=n&amp;&amp;2===n.length?n[1]:""}catch(t){}finally{return o}}e.getParamFromUrl=n,e.getSPMFromUrl=function(t){return n("spm",t)}},function(t,e,n){"us
e strict";var o=null,a=n(49).nameStorage,r=n(9);e.getRefer=function(){if(null!==o)return o;var t=r.KEY||{},e=t.NAME_STORAGE||{};return o=document.refe
rrer||a.getItem(e.REFERRER)||""}},function(t,e){"use strict";var n=function(){function t(){var t,e=[],r=!0;for(var l in p)p.hasOwnProperty(l)&amp;&amp
;(r=!1,t=p[l]||"",e.push(c(l)+s+c(t)));n.name=r?o:a+c(o)+i+e.join(u)}function e(t,e,n){t&amp;&amp;(t.addEventListener?t.addEventListener(e,n,!1):t.att
achEvent&amp;&amp;t.attachEvent("on"+e,function(e){n.call(t,e)}))}var n=window;if(n.nameStorage)return n.nameStorage;var o,a="nameStorage:",r=/^([^=]+
)(?:=(.*))?$/,i="?",s="=",u="&amp;",c=encodeURIComponent,l=decodeURIComponent,p={},g={};return function(t){if(t&amp;&amp;0===t.indexOf(a)){var e=t.spl
it(/[:?]/);e.shift(),o=l(e.shift())||"";for(var n,i,s,c=e.join(""),g=c.split(u),f=0,d=g.length;f&lt;d;f++)n=g[f].match(r),n&amp;&amp;n[1]&amp;&amp;(i=
l(n[1]),s=l(n[2])||"",p[i]=s)}else o=t||""}(n.name),g.setItem=function(e,n){e&amp;&amp;"undefined"!=typeof n&amp;&amp;(p[e]=String(n),t())},g.getItem=
function(t){return p.hasOwnProperty(t)?p[t]:null},g.removeItem=function(e){p.hasOwnProperty(e)&amp;&amp;(p[e]=null,delete p[e],t())},g.clear=function(
){p={},t()},g.valueOf=function(){return p},g.toString=function(){var t=n.name;return 0===t.indexOf(a)?t:a+t},e(n,"beforeunload",function(){t()}),g}();
e.nameStorage=n},function(t,e,n){"use strict";var o=n(42);t.exports=function(){return{init:function(t){this.options=t},updateBasicParams:function(){va
r t=this.options.context.what_to_sendpv.pvdata||[],e=this.options.context.etag||{};return e.cna&amp;&amp;(o.updateKey(t,"cna",e.cna),this.options.cont
ext.what_to_sendpv.pvdata=t),t},addTagParams:function(){var t=this.options.context.what_to_sendpv.pvdata||[],e=this.options.context.etag||{},n=[];(e.t
ag||0===e.tag)&amp;&amp;n.push(["tag",e.tag]),(e.stag||0===e.stag)&amp;&amp;n.push(["stag",e.stag]),(e.lstag||0===e.lstag)&amp;&amp;n.push(["lstag",e.
lstag]),n.length&gt;0&amp;&amp;(this.options.context.what_to_sendpv.pvdata=t.concat(n))},run:function(){this.updateBasicParams(),this.addTagParams()}}
}},function(t,e,n){"use strict";function o(t){var e,n,o,a,i=[],s={};for(e=t.length-1;e&gt;=0;e--)n=t[e],o=n[0],o&amp;&amp;o.indexOf(r.s_plain_obj)==-1
&amp;&amp;s.hasOwnProperty(o)||(a=n[1],("aplus"==o||a)&amp;&amp;(i.unshift([o,a]),s[o]=1));return i}function a(t){var e,n,o,a,s=[],u={logtype:!0,cache
:!0,scr:!0,"spm-cnt":!0};for(e=t.length-1;e&gt;=0;e--)if(n=t[e],o=n[0],a=n[1],!(i.isStartWith(o,r.s_plain_obj)&amp;&amp;!i.isStartWith(o,r.mkPlainKeyF
orExparams())||u[o]))if(i.isStartWith(o,r.mkPlainKeyForExparams())){var c=r.param2arr(a);if("object"==typeof c&amp;&amp;c.length&gt;0)for(var l=c.leng
th-1;l&gt;=0;l--){var p=c[l];p&amp;&amp;p[1]&amp;&amp;s.unshift([p[0],p[1]])}}else s.unshift([o,a]);return s}var r=n(20),i=n(13),s=n(28),u=n(35),c=n(3
4),l=n(8),p=n(14);t.exports=function(){return{init:function(t){this.options=t},getToUtData:function(t,e){var n,i=s.getGoldlogVal("_$")||{},g=i.spm||{}
,f=a(o(t)),d={};try{var h=r.arr2obj(f);h._toUT=1,h._bridgeName=e.bridgeName||"",n=JSON.stringify(h)}catch(t){n='{"_toUT":1}'}var _=u.getOnePageInfo(c)
;return d.functype="2001",d.urlpagename=_.urlpagename,d.url=location.href,d.spmcnt=g.spm_cnt||"",d.spmpre=g.spm_pre||"",d.lzsid="",d.cna=p.getCookie("
cna"),d.extendargs=n,d.isonepage=_.isonepage,d.version=l.toUtVersion,d.lver=goldlog.lver||l.lver,d.jsver=l.script_name,d},run:function(){var t=this.op
tions.context||{},e=t.what_to_sendpv||{},n=e.pvdata||[],o=t.what_to_sendpv_ut||{},a=t.where_to_sendlog_ut||{},r=a.aplusToUT||{},i=r.toUT||{};i&amp;&am
p;i.isAvailable&amp;&amp;"function"==typeof i.toUT2&amp;&amp;(o.pvdataToUt=this.getToUtData(n,i),this.options.context.what_to_sendpv_ut=o)}}}},functio
n(t,e){"use strict";t.exports=function(){return{init:function(t){this.options=t},run:function(){var t=this.options.context||{},e=t.is_single?"1":"0",n
=t.where_to_sendlog_ut||{},o=n.aplusToUT||{},a=o.toUT2||{},r=o.toUT||{};a&amp;&amp;a.isAvailable&amp;&amp;"function"==typeof a.toUT2&amp;&amp;(t.what_
to_sendpv_ut2.pvdataToUt._slog=e),r&amp;&amp;r.isAvailable&amp;&amp;"function"==typeof r.toUT2&amp;&amp;(t.what_to_sendpv_ut.pvdataToUt._slog=e),t.wha
t_to_sendpv.pvdata.push(["_slog",e])}}}},function(t,e,n){"use strict";var o=n(28);t.exports=function(){return{init:function(t){this.options=t},run:fun
ction(){var t=o.getGoldlogVal("_$")||{},e=this.options.context.can_to_sendpv||{},n=t.send_pv_count||0,a=this.options.config||{};return a.is_auto&amp;&
amp;n&gt;0?"done":(e.flag="YES",this.options.context.can_to_sendpv=e,t.send_pv_count=++n,void o.setGoldlogVal("_$",t))}}}},function(t,e,n){"use strict
";var o=n(20),a=n(28),r=n(34);t.exports=function(){return{init:function(t){this.options=t},getMetaInfo:function(){var t=a.getGoldlogVal("_$")||{},e=t.
meta_info||r.getInfo();return e},getAplusMetaByKey:function(t){var e=this.getMetaInfo()||{};return e[t]},getGifPath:function(t,e){var n,r=a.getGoldlog
Val("_$")||{};if("function"==typeof t)n=t(location.hostname,r.is_terminal,o.is_in_iframe)+".gif";else if(!n&amp;&amp;e){var i=e.match(/\/\w+\.gif/);i&
amp;&amp;i.length&gt;0&amp;&amp;(n=i[0])}return n||(n=r.is_terminal?"m.gif":"v.gif"),n},run:function(){var t=!!this.options.context.is_single;if(!t){v
ar e=this.getAplusMetaByKey("aplus-rhost-v"),n=this.options.context.where_to_sendpv||{},a=n.url||"",r=this.getGifPath(n.urlRule,a),i=o.getPvUrl({metaN
ame:"aplus-rhost-v",metaValue:e,gifPath:r,url:o.filterIntUrl(a)});n.url=i,this.options.context.where_to_sendpv=n}}}}},function(t,e,n){"use strict";var
 o=n(28),a=n(20);t.exports=function(){return{init:function(t){this.options=t},run:function(){var t=this.options.context||{},e=!!t.is_single;if(!e){var
 n=t.what_to_sendpv||{},r=t.where_to_sendpv||{},i=n.pvdata||[],s=goldlog.send(r.url,a.arr2obj(i));o.setGoldlogVal("req",s)}}}}},function(t,e){"use str
ict";t.exports=function(){return{init:function(t){this.options=t},run:function(t,e){var n=this,o=this.options.context||{},a=o.what_to_sendpv_ut||{},r=
o.where_to_sendlog_ut||{},i=a.pvdataToUt||{},s=r.aplusToUT||{},u=s.toUT;if(goldlog.isUT4Aplus&amp;&amp;"UT4Aplus"===goldlog.getMetaInfo("aplus-toUT"))
return s.toutflag="toUT",void(n.options.context.what_to_sendpv_ut.isSuccess=!0);if(u&amp;&amp;"function"==typeof u.toUT2&amp;&amp;u.isAvailable)try{s.
toutflag="toUT",u.toUT2(i,function(){n.options.context.what_to_sendpv_ut.isSuccess=!0,e()},function(t){n.options.context.what_to_sendpv_ut.errorMsg=t,
e()},2e3)}catch(t){e()}finally{return"pause"}}}}},function(t,e,n){"use strict";var o=n(20),a=n(28),r=n(58);t.exports=function(){return{init:function(t
){this.options=t},run:function(){var t=a.getGoldlogVal("_$")||{},e=t.spm||{},n=e.data||{};if(1===goldlog._$.send_pv_count){var i=n.a,s=i+"."+n.b;o.is_
in_iframe||goldlog._$.is_terminal||"a21bo.7724922"!=s&amp;&amp;"2013"!=i&amp;&amp;"a220o"!=i||r.create("//cookiemapping.wrating.com/link.html")}}}}},f
unction(t,e){"use strict";var n=document,o={};o.create=function(t,e){var o=n.createElement("iframe");o.style.width="1px",o.style.height="1px",o.style.
position="absolute",o.style.display="none",o.src=t,e&amp;&amp;(o.name=e);var a=n.getElementsByTagName("body")[0];return a.appendChild(o),o},t.exports=
o},function(t,e,n){"use strict";var o=n(7),a=n(28);t.exports=function(){return{init:function(t){this.options=t},run:function(){var t=goldlog._$||{},e=
this.options.context||{};a.setGoldlogVal("pv_context",e);var n=goldlog.spm_ab||[],r=n.join("."),i=t.send_pv_count,s={cna:e.etag.cna,count:i,spmab_pre:
goldlog.spmab_pre};o.doPubMsg(["sendPV","complete",r,s]),o.doCachePubs(["sendPV","complete",r,s])}}}},function(t,e){"use strict";e.plugins_prepv=[]},f
unction(t,e,n){"use strict";function o(){var t=i.getGoldlogVal("_$")||{},e="//gm.mmstat.com/";return t.is_terminal&amp;&amp;(e="//wgo.mmstat.com/"),{w
here_to_hjlj:{url:e,ac_atpanel:"//ac.mmstat.com/",tblogUrl:"//log.mmstat.com/"}}}function a(){return r.assign(new s,new o)}var r=n(13),i=n(28),s=n(62)
;t.exports=a},function(t,e,n){"use strict";function o(){return{compose:{},basic_params:{cna:a.getCookie("cna")},where_to_hjlj:{url:"//gm.mmstat.com/",
ac_atpanel:"//ac.mmstat.com/",tblogUrl:"//log.mmstat.com/"},userdata:{},what_to_hjlj:{logdata:{}},what_to_pvhash:{hash:[]},what_to_hjlj_exinfo:{EXPARA
MS_FLAG:"EXPARAMS",exinfo:[],exparams_key_names:["uidaplus","pc_i","pu_i"]},what_to_hjlj_ut:{logdataToUT:{}},what_to_hjlj_ut2:{isSuccess:!1,logdataToU
T:{}},where_to_sendlog_ut:{aplusToUT:{},toUTName:"toUT"},network:{connType:"UNKNOWN"},is_single:!1}}var a=n(14);t.exports=o},function(t,e,n){"use stri
ct";e.plugins_hjlj=[{name:"where_to_sendlog_ut",enable:!0,path:n(36)},{name:"is_single",enable:!0,path:n(37)},{name:"what_to_hjlj_exinfo",enable:!0,pa
th:n(64)},{name:"what_to_pvhash",enable:!0,path:n(40)},{name:"what_to_hjlj",enable:!0,path:n(65),deps:["what_to_hjlj_exinfo","what_to_pvhash"]},{name:
"what_to_hjlj_ut",enable:!0,path:n(66),deps:["is_single","what_to_hjlj_exinfo"]},{name:"what_to_hjlj_slog",enable:!0,path:n(67),deps:["what_to_hjlj"]}
,{name:"where_to_hjlj",enable:!0,path:n(68),deps:["is_single","what_to_hjlj"]},{name:"do_sendhjlj",enable:!0,path:n(69),deps:["is_single","what_to_hjl
j","where_to_hjlj"]},{name:"do_sendhjlj_ut",enable:!0,path:n(70),deps:["what_to_hjlj","what_to_hjlj_ut","where_to_sendlog_ut"]}]},function(t,e,n){"use
 strict";var o=n(20),a=n(27),r=n(28),i=n(28),s=n(26),u=n(14);t.exports=function(){return{init:function(t){this.options=t},getCookieUserInfo:function()
{var t=[],e=u.getCookie("workno")||u.getCookie("emplId");e&amp;&amp;t.push("workno="+e);var n=u.getHng();return n&amp;&amp;t.push("_hng="+u.getHng()),
t},filterExinfo:function(t){var e="";try{t&amp;&amp;("string"==typeof t?e=t.replace(/&amp;amp;/g,"&amp;").replace(/\buserid=/,"uidaplus=").replace(/&a
mp;aplus&amp;/,"&amp;"):"object"==typeof t&amp;&amp;(e=o.obj2param(t,!0)))}catch(t){e=t.message?t.message:""}return e},getExparamsFlag:function(){var
t=this.options.context||{},e=t.what_to_hjlj_exinfo||{};return e.EXPARAMS_FLAG||"EXPARAMS"},getCustomExParams:function(t){var e="";return t!==this.getE
xparamsFlag()&amp;&amp;(e=this.filterExinfo(t)||""),e?e.split("&amp;"):[]},getBeaconExparams:function(t,e){var n=[],r=a.getExParams(o)||"";r=r.replace
(/&amp;aplus&amp;/,"&amp;");for(var i=o.param2arr(r)||[],u=function(e){return s.indexof(t,e)&gt;-1},c=0;c&lt;i.length;c++){var l=i[c],p=l[0]||"",g=l[1
]||"";p&amp;&amp;g&amp;&amp;(e===this.getExparamsFlag()||u(p))&amp;&amp;n.push(p+"="+g)}return n},getExinfo:function(t){var e=this.options.context||{}
,n=e.what_to_hjlj_exinfo||{},o=n.exparams_key_names||[],a=this.getBeaconExparams(o,t);return a},getExData:function(t){var e=[];if("object"==typeof t)f
or(var n in t){var o=t[n];n&amp;&amp;o&amp;&amp;"object"!=typeof o&amp;&amp;"function"!=typeof o&amp;&amp;e.push(n+"="+o)}return e},doConcatArr:functi
on(t,e){return e&amp;&amp;e.length&gt;0&amp;&amp;(t=t.concat(e)),t},run:function(){try{var t=this.options.context.what_to_hjlj_exinfo||{},e=r.getGoldl
ogVal("_$")||{},n=e.meta_info||{},o=n["aplus-exinfo"]||"",a=n["aplus-exdata"]||"",s=[];s=this.doConcatArr(s,t.exinfo||[]),s=this.doConcatArr(s,this.ge
tExinfo(o)),s=this.doConcatArr(s,this.getCookieUserInfo()),s=this.doConcatArr(s,this.getCustomExParams(o)),s=this.doConcatArr(s,this.getExData(a)),t.e
xinfo=s.join("&amp;"),this.options.context.what_to_hjlj_exinfo=t}catch(t){i.logger({msg:t?t.message:""})}}}}},function(t,e,n){"use strict";var o=n(27)
,a=n(20),r=n(13);t.exports=function(){return{init:function(t){this.options=t},getParams:function(){var t=this.options.context||{},e=t.userdata||{},n=t
.basic_params||{},i=t.what_to_hjlj_exinfo||{},s=i.exinfo||"";e.gokey&amp;&amp;s&amp;&amp;0!==s.indexOf("&amp;")&amp;&amp;(s="&amp;"+s);var u=n.cna,c=e
.gmkey,l=e.gokey||"";l+=s;var p=t.what_to_pvhash||{},g=p.hash||[];g.length&amp;&amp;(l+="&amp;"+g.join("="));var f={cache:r.makeCacheNum(),gmkey:c,gok
ey:l,cna:u};e["spm-cnt"]&amp;&amp;(f["spm-cnt"]=e["spm-cnt"]),e["spm-pre"]&amp;&amp;(f["spm-pre"]=e["spm-pre"]);try{var d=o.getExParams(a),h=a.param2o
bj(d).uidaplus;h&amp;&amp;(f._gr_uid_=h)}catch(t){}return f},run:function(){this.options.context.what_to_hjlj.logdata=this.getParams()}}}},function(t,
e,n){"use strict";var o=n(38),a=n(14),r=n(28),i=n(8);t.exports=function(){return{init:function(t){this.options=t},getToUtData:function(t,e){var n=r.ge
tGoldlogVal("_$")||{},s=n.spm||{},u=this.options.context||{},c=u.userdata||{},l=u.what_to_hjlj_exinfo||{},p=l.exinfo||"";c.gokey&amp;&amp;p&amp;&amp;0
!==p.indexOf("&amp;")&amp;&amp;(p="&amp;"+p);var g=c.gokey+p,f={gmkey:c.gmkey,gokey:g,lver:i.lver,jsver:i.script_name,version:i.toUtVersion,spm_cnt:s.
spm_cnt||"",spm_url:s.spm_url||"",spm_pre:s.spm_pre||""};t&amp;&amp;(f._is_g2u_=1),f._bridgeName=e.bridgeName||"",f._toUT=1;try{f=JSON.stringify(f),"{
}"==f&amp;&amp;(f="")}catch(t){f=""}var d=n.meta_info||{},h=d.isonepage_data||{},_={};return _.functype=o.getFunctypeValue({logkey:c.logkey,gmkey:c.gm
key,spm_ab:r.getGoldlogVal("spm_ab")}),_.spmcnt=s.spm_cnt||"",_.spmurl=s.spm_url||"",_.spmpre=s.spm_pre||"",_.logkey=c.logkey,_.logkeyargs=f,_.urlpage
name=h.urlpagename,_.url=location.href,_.cna=a.getCookie("cna")||"",_.extendargs="",_.isonepage=h.isonepage,_},run:function(){var t=this.options.conte
xt||{},e=!!t.is_single,n=t.what_to_hjlj_ut||{},o=t.where_to_sendlog_ut||{},a=o.aplusToUT||{},r=a.toUT||{};n.logdataToUT=this.getToUtData(e,r),this.opt
ions.context.what_to_hjlj_ut=n}}}},function(t,e){"use strict";t.exports=function(){return{init:function(t){this.options=t},run:function(){var t=this.o
ptions.context||{},e=t.is_single?"1":"0",n=t.where_to_sendlog_ut||{},o=n.aplusToUT||{},a=o.toUT2||{},r=o.toUT||{};a&amp;&amp;a.isAvailable&amp;&amp;"f
unction"==typeof a.toUT2&amp;&amp;(t.what_to_hjlj_ut2.logdataToUT._slog=e),r&amp;&amp;r.isAvailable&amp;&amp;"function"==typeof r.toUT2&amp;&amp;(t.wh
at_to_hjlj_ut.logdataToUT._slog=e),t.what_to_hjlj.logdata.gokey?t.what_to_hjlj.logdata.gokey+="&amp;_slog="+e:t.what_to_hjlj.logdata.gokey="_slog="+e}
}}},function(t,e,n){"use strict";var o=n(20),a=n(13),r=n(28),i=n(25),s=n(34);t.exports=function(){return{init:function(t){this.options=t},getMetaInfo:
function(){var t=r.getGoldlogVal("_$")||{},e=t.meta_info||s.getInfo();return e},getAplusMetaByKey:function(t){var e=this.getMetaInfo()||{};return e[t]
},cramUrl:function(t){var e=r.getGoldlogVal("_$")||{},n=e.spm||{},o=this.options.context.where_to_hjlj||{},i=o.ac_atpanel,s=o.tblogUrl,u=this.options.
context.what_to_hjlj||{},c=this.options.context.userdata||{},l=!0,p=c.logkey;if(!p)return{url:t,logkey_available:!1};if("ac"==p)t=i+"1.gif";else if(a.
isStartWith(p,"ac-"))t=i+p.substr(3);else if(a.isStartWith(p,"/")){t+=p.substr(1);var g=u.logdata||{};g["spm-cnt"]=n.spm_cnt,g.logtype=2;try{u.logdata
=g,this.options.context.what_to_hjlj=u}catch(t){}}else a.isEndWith(p,".gif")?t=s+p:l=!1;return{url:t,logkey_available:l}},can_to_sendhjlj:function(t){
var e=this.options.context||{},n=e.logger||function(){},o=this.options.context.userdata||{};return!!t.logkey_available||(n({msg:"logkey: "+o.logkey+"
is not legal!"}),!1)},run:function(){var t=!!this.options.context.is_single;if(!t){var e,n,a=o.filterIntUrl(this.options.context.where_to_hjlj.url),r=
this.getAplusMetaByKey("aplus-rhost-g"),s=r&amp;&amp;o.hostValidity(r);s&amp;&amp;(e=/^\/\//.test(r)?"":"//",n=/\/$/.test(r)?"":"/",a=e+r+n),r&amp;&am
p;!s&amp;&amp;i.logger({msg:"aplus-rhost-g: "+r+' is invalid, suggestion: "xxx.mmstat.com"'});var u=this.cramUrl(a);return this.can_to_sendhjlj(u)?voi
d(this.options.context.where_to_hjlj.url=u.url):"done"}}}}},function(t,e,n){"use strict";var o=n(28);t.exports=function(){return{init:function(t){this
.options=t},run:function(){var t=this.options.context||{},e=this.options.config||{},n=!!t.is_single;if(!n){var a=t.logger||{},r=t.what_to_hjlj||{},i=t
.where_to_hjlj||{},s=r.logdata||{},u=i.url||"";u||"function"!=typeof a||a({msg:"warning: where_to_hjlj.url is null, goldlog.record failed!"});var c=go
ldlog.send(i.url,s,e.method||"GET");o.setGoldlogVal("req",c)}}}}},function(t,e){"use strict";t.exports=function(){return{init:function(t){this.options
=t},run:function(t,e){var n=this,o=this.options.context||{},a=o.what_to_hjlj_ut2.isSuccess,r=o.logger||function(){},i=!!o.is_single,s=o.where_to_sendl
og_ut||{},u=o.what_to_hjlj_ut||{},c=u.logdataToUT||{},l=s.aplusToUT||{},p=l.toUT;if(goldlog.isUT4Aplus&amp;&amp;"UT4Aplus"===goldlog.getMetaInfo("aplu
s-toUT"))return l.toutflag="toUT",void(n.options.context.what_to_hjlj_ut.isSuccess=!0);if(!a&amp;&amp;p&amp;&amp;"function"==typeof p.toUT2&amp;&amp;p
.isAvailable)try{l.toutflag="toUT",p.toUT2(c,function(){n.options.context.what_to_hjlj_ut.isSuccess=!0,e()},function(t){n.options.context.what_to_hjlj
_ut.errorMsg=t,e()},3e3)}catch(t){i&amp;&amp;r({msg:"warning: singleSend toUTName = "+s.toUTName+" errorMsg:"+t.message})}finally{return"pause"}}}}},f
unction(t,e,n){"use strict";function o(){var t,e,n=i.KEY||{},o=n.NAME_STORAGE||{};if(!c&amp;&amp;u){var a=location.href,l=u&amp;&amp;(a.indexOf("login
.taobao.com")&gt;=0||a.indexOf("login.tmall.com")&gt;=0),p=s.getRefer();l&amp;&amp;p?(t=p,e=r.getItem(o.REFERRER_PV_ID)):(t=a,e=goldlog.pvid),r.setIte
m(o.REFERRER,t),r.setItem(o.REFERRER_PV_ID,e)}}var a=n(72),r=n(49).nameStorage,i=n(8),s=n(48),u="https:"==location.protocol,c=parent!==self;e.run=func
tion(){a.on(window,"beforeunload",function(){o()})}},function(t,e){"use strict";function n(t,e){var n=goldlog._$||{},o=n.meta_info||{},a=o.aplus_ctap|
|{};if(a&amp;&amp;"function"==typeof a.on)a.on(t,e);else{var r="ontouchend"in document.createElement("div"),i=r?"touchstart":"mousedown";s(t,i,e)}}fun
ction o(t){try{c.documentElement.doScroll("left")}catch(e){return void setTimeout(function(){o(t)},1)}t()}function a(t){var e=0,n=function(){0===e&amp
;&amp;t(),e++};"complete"===c.readyState&amp;&amp;n();var a;if(c.addEventListener)a=function(){c.removeEventListener("DOMContentLoaded",a,!1),n()},c.a
ddEventListener("DOMContentLoaded",a,!1),window.addEventListener("load",n,!1);else if(c.attachEvent){a=function(){"complete"===c.readyState&amp;&amp;(
c.detachEvent("onreadystatechange",a),n())},c.attachEvent("onreadystatechange",a),window.attachEvent("onload",n);var r=!1;try{r=null===window.frameEle
ment}catch(t){}c.documentElement.doScroll&amp;&amp;r&amp;&amp;o(n)}}function r(t){"complete"===c.readyState?t():s(u,"load",t)}function i(t){if(!/touch
|mouse|scroll|wheel/i.test(t))return!1;var e=!1;try{var n=Object.defineProperty({},"passive",{get:function(){e=!0}});u.addEventListener("test",null,n)
}catch(t){}return e}function s(){var t=arguments;if(2===t.length)"DOMReady"===t[0]&amp;&amp;a(t[1]),"onload"===t[0]&amp;&amp;r(t[1]);else if(3===t.len
gth){var e=t[0],o=t[1],s=t[2];"tap"===o?n(e,s):e[f]((l?"on":"")+o,function(t){t=t||u.event;var e=t.target||t.srcElement;"function"==typeof s&amp;&amp;
s(t,e)},!!i(o)&amp;&amp;{passive:!0})}}var u=window,c=document,l=!!c.attachEvent,p="attachEvent",g="addEventListener",f=l?p:g;e.DOMReady=a,e.onload=r,
e.on=s},function(t,e,n){"use strict";function o(){var t,e="_ap",n=r[e]=r[e]||[];n.push=t=function(){var t="0.0";window.goldlog&amp;&amp;window.goldlog
.spm_ab&amp;&amp;(t=window.goldlog.spm_ab.join(".")),f.do_tracker_obsolete_inter({ratio:d?1:.01,page:location.hostname+location.pathname,spm_ab:t,inte
rface_name:"win._ap",interface_params:JSON.stringify(arguments)});for(var e,o,a=0,r=arguments.length;a&lt;r;a++)e=arguments[a],s.isString(e)?goldlog.s
end(l.hjlj()+e):s.isArray(e)&amp;&amp;"push"!=(o=e[0])&amp;&amp;(n[o]=n[o]||[]).push(e.slice(1))};for(var o;o=n.shift();)t(o)}function a(){var t=(new
Date).getTime(),e=Math.floor(t/72e5),n=i.getElementById("aplus-sufei"),o=goldlog._$||{},a=goldlog.getCdnPath(),r=a+"/alilog/aplus_plugin_xwj/index.js?
t="+e,s=a+"/alilog/oneplus/entry.js?t="+e,l=a+"/alilog/stat/a.js?t="+e,p=a+"/secdev/entry/index.js?t="+e,g=a+"/alilog/mlog/wp_beacon.js?t="+e,f=o.meta
_info,d=function(){u.addScript(l),u.addScript(g),u.addScript(r),u.addScript(s)},h=function(){Math.random()&lt;.01&amp;&amp;u.addScript(l),f.ms_data_in
stance_id&amp;&amp;f.ms_prototype_id&amp;&amp;f.ms_prototype_id.match(/^[124]$/)&amp;&amp;f.ms_data_shop_id&amp;&amp;u.addScript(g);var t=f["aplus-rat
e-ahot"];(Math.random()&lt;t||f["ahot-aplus"])&amp;&amp;u.addScript(r),u.addScript(s)},_=f["aplus-xplug"];c.onload(function(){try{switch(_){case"NONE"
:break;case"ALL":d();break;default:h()}}catch(t){}}),"NONE"!==_&amp;&amp;setTimeout(function(){n&amp;&amp;"script"==n.tagName.toLowerCase()||u.addScri
pt(p,"","aplus-sufei")},10)}var r=window,i=document,s=n(13),u=n(27),c=n(72),l=n(74),p=n(25),g=n(75),f=n(77),d=p.isDebugAplus();e.run=function(){o(),a(
)},e.init_watchGoldlogQueue=g.init_watchGoldlogQueue},function(t,e,n){"use strict";var o=n(23);e.hjlj=function(){var t=window.goldlog||(window.goldlog
={}),e=t._$||{},n=e.script_name,a=e.meta_info||{},r=a["aplus-rhost-g"],i="//gm.mmstat.com/";return(e.is_terminal||"aplus_wap"===n)&amp;&amp;(i="//wgo.
mmstat.com/"),"aplus_int"===n&amp;&amp;(i="//gj.mmstat.com/"),r&amp;&amp;(i="//"+r+"/"),o.getProtocal()+i}},function(t,e,n){"use strict";var o=window,
a=n(13),r=n(74),i=n(25),s=n(4),u=n(76),c=n(77),l=i.isDebugAplus();e.init_aplusQueue=function(){var t,e="_ap",n=o[e]=o[e]||[];n.push=t=function(){var t
="0.0";window.goldlog&amp;&amp;window.goldlog.spm_ab&amp;&amp;(t=window.goldlog.spm_ab.join(".")),c.do_tracker_obsolete_inter({ratio:l?1:.01,page:loca
tion.hostname+location.pathname,spm_ab:t,interface_name:"win._ap",interface_params:JSON.stringify(arguments)});for(var e,o,i=0,s=arguments.length;i&lt
;s;i++)e=arguments[i],a.isString(e)?goldlog.send(r.hjlj()+e):a.isArray(e)&amp;&amp;"push"!=(o=e[0])&amp;&amp;(n[o]=n[o]||[]).push(e.slice(1))};for(var
 i;i=n.shift();)t(i)};var p="goldlog_queue",g=function(t){try{if(t&amp;&amp;t.action&amp;&amp;t.arguments&amp;&amp;a.isArray(t.arguments)){var e=t.act
ion.split("."),n=o,r=o;if(3===e.length)n=o[e[0]][e[1]],r=n[e[2]];else for(;e.length;)if(r=n=n[e.shift()],!n)return;"function"==typeof r&amp;&amp;r.app
ly(n,t.arguments)}}catch(t){}},f=function(t){function e(){var t=o[p];if(t&amp;&amp;a.isArray(t)&amp;&amp;t.length){o[p]&amp;&amp;a.isArray(o[p])||(o[p
]=[]);for(var e={};e=t.shift();)e&amp;&amp;e.action&amp;&amp;e.arguments&amp;&amp;a.isArray(e.arguments)&amp;&amp;g(e)}}try{e()}catch(t){}finally{"fun
ction"==typeof t&amp;&amp;t()}};e.processGoldlogQueue=f;var d=s.extend({push:function(t){this.length++,g(t)}}),h=function(){o[p]=d.create({length:0})}
,_=function(t){for(var e=0,n=0;n&lt;t.length;n++)t[n]||e++;return e===t.length};e.init_watchGoldlogQueue=function(){u.init_loadAplusPlugin();try{var t
=o[p]||[];!t||0===t.length||_(t||[])?h():f(function(){h()})}catch(t){}}},function(t,e,n){"use strict";var o=n(27),a=n(35),r=n(10),i=function(t,e){var
n=a.getMetaCnt(t);return!(!n&amp;&amp;!e)},s=function(){var t=goldlog.getCdnPath();return{aplus_ae_path:t+"/alilog/s/"+r.lver+"/plugin/aplus_ae.js",ap
lus_ac_path:t+"/alilog/s/"+r.lver+"/plugin/aplus_ac.js"}},u=function(t,e){var n=s(),a=i(t,e),r={"aplus-auto-exp":n.aplus_ae_path,"aplus-auto-clk":n.ap
lus_ac_path};a&amp;&amp;r[t]&amp;&amp;o.addScript(r[t])};e.init_loadAplusPlugin=function(){!goldlog._aplus_auto_exp&amp;&amp;u("aplus-auto-exp"),!gold
log._aplus_ac&amp;&amp;u("aplus-auto-clk"),goldlog.aplus_pubsub.subscribe("setMetaInfo",function(t,e){"aplus-auto-exp"!==t||goldlog._aplus_auto_exp||u
(t,e),"aplus-auto-clk"!==t||goldlog._aplus_ac||u(t,e)})}},function(t,e,n){"use strict";var o=n(25),a=function(t,e,n){try{var a=window.goldlog_queue||(
window.goldlog_queue=[]);a.push({action:["goldlog","_aplus_cplugin_m",e].join("."),arguments:[t,n]})}catch(t){o.logger({msg:t})}};e.do_tracker_jserror
=function(t,e){a(t,"do_tracker_jserror",e)},e.do_tracker_obsolete_inter=function(t,e){a(t,"do_tracker_obsolete_inter",e)},e.wrap=function(t){if("funct
ion"==typeof t)try{t()}catch(t){o.logger({msg:t.message||t})}finally{}}},function(t,e){"use strict";function n(t,e){return t.indexOf(e)&gt;-1}function
 o(t,e){for(var o=0,a=t.length;o&lt;a;o++)if(n(e,t[o]))return!0;return!1}var a=location.host,r=["xiaobai.com","admin.taobao.org","aliloan.com","mybank
.cn"],i=["tmc.admin.taobao.org","tmall.admin.taobao.org"];e.is_exception=o(r,a)&amp;&amp;!o(i,a)},function(t,e,n){"use strict";function o(){var t,e,n,
o,a=c.getElementsByTagName("meta");for(t=0,e=a.length;t&lt;e;t++)if(n=a[t],o=n.getAttribute("name"),"data-spm"===o||"spm-id"===o)return n}function a()
{var t=c.createElement("meta");t.setAttribute("name","data-spm");var e=c.getElementsByTagName("head")[0];return e&amp;&amp;e.insertBefore(t,e.firstChi
ld),t}function r(){var t=o();t||(t=a()),t.setAttribute("content",goldlog.spm_ab[0]||"");var e=c.getElementsByTagName("body")[0];e&amp;&amp;e.setAttrib
ute("data-spm",goldlog.spm_ab[1]||"")}function i(){var t,e,n,o=c.getElementsByTagName("*");for(t=0,e=o.length;t&lt;e;t++)n=o[t],n.getAttribute("data-s
pm-max-idx")&amp;&amp;n.setAttribute("data-spm-max-idx",""),n.getAttribute("data-spm-anchor-id")&amp;&amp;n.setAttribute("data-spm-anchor-id","")}func
tion s(){var t=5e3;try{var e=goldlog.getMetaInfo("aplus-mmstat-timeout");if(e){var n=parseInt(e);n&gt;=1e3&amp;&amp;n&lt;=1e4&amp;&amp;(t=n)}}catch(t)
{}return t}var u=window,c=document,l=n(4),p=n(20),g=n(72),f=n(25),d=n(7),h=n(13),_=n(28),m=n(23),v=n(6),b=n(46),y=n(34),w=y.getInfo(),x=n(8),j=n(77),T
=n(80),P=n(14),S=n(83),A=f.isDebugAplus(),k=[],E=[],U=[],C=[],I=function(t,e){var n=new Image,o="_img_"+Math.random(),a=p.makeUrl(t,e);u[o]=n;var r=fu
nction(){if(u[o])try{delete u[o]}catch(t){u[o]=void 0}};return n.onload=function(){r()},n.onerror=function(){r()},setTimeout(function(){window[o]&amp;
&amp;(window[o].src="",r())},s()),n.src=a,n=null,a},M=function(t,e){for(var n in e)"cna"!==n&amp;&amp;(e[n]=encodeURIComponent(e[n]));return navigator
.sendBeacon(t,JSON.stringify(e)),t};e.run=l.extend({getCdnPath:function(){var t=c.getElementById("beacon-aplus")||c.getElementById("tb-beacon-aplus"),
e="//g.alicdn.com",n=["//assets.alicdn.com/g","//g-assets.daily.taobao.net"];if(t)for(var o=0;o&lt;n.length;o++){var a=new RegExp(n[o]);if(a.test(t.sr
                <span class="min-order-count">50 Piece/Pieces</span>
                <span class="min-order-unit"></span>
            </div>
        </div>
    </div>
    <div class="product-item util-clearfix">
        <div class="selector util-left">
            <input type="checkbox" name="id" value="60518968485" data-idf="IDX1kv_q2JJ6uVDHUGZrkgFoaFCmSH15K1c-jjKEpBQJirvqfI2fAlm1uPkLjQnC-SwO" />
        </div>
        <div class="product-image util-valign util-left">
            <a class="util-valign-ctn" href="//www.alibaba.com/product-detail/Excellent-quality-decorative-3d-bamboo-interior_60518968485.html" target
="_blank" title="Excellent quality decorative 3d bamboo interior wall paneling">
                <img class="util-valign-inner" src="//sc01.alicdn.com/kf/HTB1dK56MVXXXXXjXXXXq6xXFXXXd/Excellent-quality-decorative-3d-bamboo-interior
-wall.jpg_100x100.jpg" />
            </a>
        </div>
        <div class="product-info-wrap util-left">
            <div class="product-name">
                <a href="//www.alibaba.com/product-detail/Excellent-quality-decorative-3d-bamboo-interior_60518968485.html" class="link-normal" target
="_blank" title="Excellent quality decorative 3d bamboo interior wall paneling">
                    Excellent quality decorative 3d bamboo interior wall paneling
                </a>
            </div>
            <div class="product-price">
                US $ 7 - 15
            </div>
            <div class="product-min-order">
                <span class="min-order-count">1 Roll/Rolls</span>
                <span class="min-order-unit"></span>
            </div>
        </div>
    </div>
    <div class="product-item util-clearfix">
        <div class="selector util-left">
            <input type="checkbox" name="id" value="60035143466" data-idf="IDX1KzJHsozG556ZllTvvnjTEfWTP7tPTzpJ1Jp1B0RD7P_wpVmtlHMOc0KODMDYi27K" />
        </div>
        <div class="product-image util-valign util-left">
            <a class="util-valign-ctn" href="//www.alibaba.com/product-detail/3d-exterior-wall-decor-panel_60035143466.html" target="_blank" title="3d
 exterior wall decor panel">
                <img class="util-valign-inner" src="//sc01.alicdn.com/kf/HTB1f7Gnm8HH8KJjy0Fbq6AqlpXaj/3d-exterior-wall-decor-panel.jpg_100x100.jpg" /
>
            </a>
        </div>
        <div class="product-info-wrap util-left">
            <div class="product-name">
                <a href="//www.alibaba.com/product-detail/3d-exterior-wall-decor-panel_60035143466.html" class="link-normal" target="_blank" title="3d
 exterior wall decor panel">
                    3d exterior wall decor panel
                </a>
            </div>
            <div class="product-price">
                US $ 2 - 3 / Meter
            </div>
            <div class="product-min-order">
                <span class="min-order-count">50 Meter/Meters We could check the exterior wall decor panel in stock</span>
                <span class="min-order-unit"></span>
            </div>
        </div>
    </div>
    <div class="product-item util-clearfix">
        <div class="selector util-left">
            <input type="checkbox" name="id" value="60741587989" data-idf="IDX109EAkX9430_T-eHIBjqEzrQ64n8QMFDc0xGmrVSUePkKqVZa_KqEKDsIsim-olTU" />
        </div>
        <div class="product-image util-valign util-left">
            <a class="util-valign-ctn" href="//www.alibaba.com/product-detail/2018-manufactured-home-interior-decorative-bathroom_60741587989.html" ta
rget="_blank" title="2018 manufactured home interior decorative bathroom 3d pvc composite wall panel cladding for building materials">
                <img class="util-valign-inner" src="//sc01.alicdn.com/kf/HTB1EW_VacIrBKNjSZK9q6ygoVXay/2018-manufactured-home-interior-decorative-bath
room-3d.jpg_100x100.jpg" />
            </a>
        </div>
        <div class="product-info-wrap util-left">
            <div class="product-name">
                <a href="//www.alibaba.com/product-detail/2018-manufactured-home-interior-decorative-bathroom_60741587989.html" class="link-normal" ta
rget="_blank" title="2018 manufactured home interior decorative bathroom 3d pvc composite wall panel cladding for building materials">
                    2018 manufactured home interior decorative bathroom 3d pvc composite wall panel cladding for building materials
                </a>
            </div>
            <div class="product-price">
                US $ 15 - 28 / Square Meter
            </div>
            <div class="product-min-order">
                <span class="min-order-count">300 Square Meter/Square Meters</span>
                <span class="min-order-unit"></span>
            </div>
        </div>
    </div>
    <div class="product-item util-clearfix">
        <div class="selector util-left">
            <input type="checkbox" name="id" value="60326240849" data-idf="IDX1yZt85sON2Woqig0mV6WY_dCIVW5KExm4zevkeXZ15zaeR8ViCd4DEFcVhLYDrChG" />
        </div>
        <div class="product-image util-valign util-left">
            <a class="util-valign-ctn" href="//www.alibaba.com/product-detail/2018-new-style-interior-fire-resistant_60326240849.html" target="_blank"
 title="2018 new style interior fire resistant decorative pvc 3d wall panel">
                <img class="util-valign-inner" src="//sc02.alicdn.com/kf/HTB1F6wwkA9WBuNjSspeq6yz5VXan/2018-new-style-interior-fire-resistant-decorati
ve.jpg_100x100.jpg" />
            </a>
        </div>
        <div class="product-info-wrap util-left">
            <div class="product-name">
                <a href="//www.alibaba.com/product-detail/2018-new-style-interior-fire-resistant_60326240849.html" class="link-normal" target="_blank"
 title="2018 new style interior fire resistant decorative pvc 3d wall panel">
                    2018 new style interior fire resistant decorative pvc 3d wall panel
                </a>
            </div>
            <div class="product-price">
                US $ 4.99 - 5.99
            </div>
            <div class="product-min-order">
                <span class="min-order-count">1 Square Meter/Square Meters</span>
                <span class="min-order-unit"></span>
            </div>
        </div>
    </div>
    <div class="product-item util-clearfix">
        <div class="selector util-left">
            <input type="checkbox" name="id" value="60710065303" data-idf="IDX1-xyavbw7nUcOMyLr7A11xULn-8RWMNAiUsLX0wMjXlfar7qf4RHhObcNNNdHvjgH" />
        </div>
        <div class="product-image util-valign util-left">
            <a class="util-valign-ctn" href="//www.alibaba.com/product-detail/INTCO-WATER-PROOF-QUICK-INSTALL-DECORATIVE_60710065303.html" target="_bl
ank" title="INTCO WATER PROOF QUICK INSTALL DECORATIVE 3D WALL PANEL">
                <img class="util-valign-inner" src="//sc01.alicdn.com/kf/HTB15t89b8DH8KJjSszcq6zDTFXaX/INTCO-WATER-PROOF-QUICK-INSTALL-DECORATIVE-3D.j
pg_100x100.jpg" />
            </a>
        </div>
        <div class="product-info-wrap util-left">
            <div class="product-name">
                <a href="//www.alibaba.com/product-detail/INTCO-WATER-PROOF-QUICK-INSTALL-DECORATIVE_60710065303.html" class="link-normal" target="_bl
ank" title="INTCO WATER PROOF QUICK INSTALL DECORATIVE 3D WALL PANEL">
                    INTCO WATER PROOF QUICK INSTALL DECORATIVE 3D WALL PANEL
                </a>
            </div>
            <div class="product-price">
                US $ 0.5 - 3 / Meter
            </div>
            <div class="product-min-order">
                <span class="min-order-count">1000 Meter/Meters INTCO stone finish quick install 3D wall panel</span>
                <span class="min-order-unit"></span>
            </div>
        </div>
    </div>
    <div class="product-item util-clearfix">
        <div class="selector util-left">
            <input type="checkbox" name="id" value="60648637219" data-idf="IDX1cLU9FDhEBVf3_RXqoGpRjCX_rcaT1iwokR3ghawjV-Fxc74ZH_BqBh3BQYdmUKmT" />
        </div>
        <div class="product-image util-valign util-left">
            <a class="util-valign-ctn" href="//www.alibaba.com/product-detail/300mm-Building-Waterproof-3D-PVC-Faux_60648637219.html" target="_blank"
title="300mm Building Waterproof 3D PVC Faux Marble Wall Decorative Panel for sale">
                <img class="util-valign-inner" src="//sc02.alicdn.com/kf/HTB104gBQVXXXXbeXVXXq6xXFXXXk/300mm-Building-Waterproof-3D-PVC-Faux-Marble.jp
g_100x100.jpg" />
            </a>
        </div>
        <div class="product-info-wrap util-left">
            <div class="product-name">
                <a href="//www.alibaba.com/product-detail/300mm-Building-Waterproof-3D-PVC-Faux_60648637219.html" class="link-normal" target="_blank"
title="300mm Building Waterproof 3D PVC Faux Marble Wall Decorative Panel for sale">
                    300mm Building Waterproof 3D PVC Faux Marble Wall Decorative Panel for sale
                </a>
            </div>
            <div class="product-price">
                US $ 2.63 - 2.65
            </div>
            <div class="product-min-order">
                <span class="min-order-count">2000 Meter/Meters</span>
                <span class="min-order-unit"></span>
            </div>
        </div>
    </div>
</div>
</div>
    <div class="history-footer">
        <button class="ui2-button ui2-button-primary ui2-button-medium disabled contact-button" disabled="" data-role="contactSupplier" data-domdot="i
d:3301,ext:'other=history'">Contact Supplier</button>
    </div>
    <div class="history-feedback ui2-feedback ui2-feedback-small ui2-feedback-error ui2-feedback-hasbg" data-role="history-feedback">
        <i class="ui2-icon ui2-icon-error"></i>
        <div class="ui2-feedback-content" data-role="feedback-content"></div>
    </div>
</div></div></div><!-- Add webww-contacts for oldWebATM -->
<div class="webatm2-iconbar-wrap webww-contacts sidebar-mod" id="webww-contacts" style="bottom: 76.6px; right: 28px;">
    <div class="webatm2-iconbar" id="webatm2-iconbar">
        <a class="webatm2-icon ui2-icon ui2-icon-alitalk" href="javascript:;"></a>
        <div class="webatm2-msg-num">0</div>
    </div>
    <div class="webatm2-panel" id="webatm2-panel" style="right: 28.8px;">
        <div class="webatm2-panel-top">
            <span class="webatm2-panel-title">Trade Manager</span>
            <span class="webatm2-panel-close ui2-icon ui2-icon-cross"></span>
        </div>
        <div class="webatm2-panel-body">
            <div class="webatm2-panel-tabset">
                <div class="webatm2-panel-tab tab-recent active" data-type="recent">
                    <i class="ui2-icon ui2-icon-history"></i>
                </div>
                <div class="webatm2-panel-tab tab-contact" data-type="contact">
                    <i class="ui2-icon ui2-icon-account"></i>
                </div>
                <div class="webatm2-panel-tab tab-sysmsg" data-type="sysmsg">
                    <i class="ui2-icon ui2-icon-remind"></i>
                </div>
            </div>
            <div class="webatm2-panel-content" style="height: 330px;">
                <div class="webatm2-panel-item panel-recent nano active has-scrollbar" data-type="recent">
                    <div class="nano-content" tabindex="0" style="right: -17px;"></div>
                <div class="nano-pane" style="display: none;"><div class="nano-slider" style="transform: translate(0px, 0px); height: 20px;"></div></d
iv></div>
                <div class="webatm2-panel-item panel-contact nano has-scrollbar" data-type="contact">
                    <div class="nano-content" tabindex="0" style="right: -17px;"></div>
                <div class="nano-pane" style="display: none;"><div class="nano-slider" style="transform: translate(0px, 0px); height: 20px;"></div></d
iv></div>
                <div class="webatm2-panel-item panel-sysmsg nano has-scrollbar" data-type="sysmsg">
                    <div class="nano-content" tabindex="0" style="right: -17px;"><a href="javascript:void(0);" class="webatm2-sysmsg-more">View All</a
>
</div>
                <div class="nano-pane" style="display: none;"><div class="nano-slider" style="transform: translate(0px, 0px); height: 20px;"></div></d
iv></div>
            </div>
        </div>
    </div>
    <div class="webatm2-tips">
        <span class="webatm2-tips-mark"></span>
        <span class="webatm2-tips-close">×</span>
        <span class="webatm2-tips-icon"></span>
        <div class="webatm2-tips-content"></div>
    </div>
    <div class="webatm2-confirm">
    </div>
</div><div class="webatm2-dialog close" id="webatm2-dialog" style="min-width: 700px; min-height: 500px; display: none; width: 860px; height: 560px; le
ft: 29.5px; top: 67px;">
    <div class="webatm2-drag-layer"></div>
    <div class="webatm2-dialog-tools">
        <div class="webatm2-dialog-fullscreen"></div>
        <div class="webatm2-dialog-close"></div>
    </div>
    <iframe class="webatm2-iframe" id="webatm2-iframe" src="//atmgateway-client.alibaba.com/atmgateway/webatm.htm?iframe_delete=true" frameborder="0"
marginheight="0" marginwidth="0"></iframe>
</div><div class="atm-loader-bottom-pop-wrap" id="atm-loader-bottom-pop-wrap" data-widget-cid="widget-6" style="right: 30px;">
        <div class="albpw-header">
                <span class="albpw-title" data-role="albpw-title"></span>
                <span class="albpw-close">X</span>
        </div>
        <div class="albpw-container" data-role="albpw-container">
        </div>
</div><div class="initiative-sugguestion-list with-toolbar" id="initiative-sugguestion-list" data-widget-cid="widget-7" style="right: 38px; bottom: 61
.6px;"></div><iframe id="sem-remarketing" name="sem-remarketing" src="https://i.alicdn.com/sc-affiliate/sem-remarketing/proxy.8144c682.html?iframe_del
ete=true" style="display: none; visibility: hidden;"></iframe></body></html>

'''

from bs4 import BeautifulSoup

# soup=BeautifulSoup(i,'lxml')
# market=soup.select('.container-table')
# print(market)
# 创建chrome参数对象
opt = webdriver.ChromeOptions()
# 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
opt.set_headless()
# 创建chrome无界面对象
# browser = webdriver.Chrome()
# browser.implicitly_wait(30)  # 隐性等待，最长等30秒 # 创建chrome参数对象

url = 'https://www.alibaba.com/product-detail/Hot-Selling-Patented-Product-exterior-3d_60451064794.html'
id='60648637219'
url2 = 'https://www.alibaba.com/view/mutiapps/mutiapps.htm?data=%5B%7B%22module_name%22%3A%22supplierBasicInformation%22%2C%22module_data%22%3A%7B%7D%7D%2C%7B%22module_name%22%3A%22supplierAndProductSamples%22%2C%22module_data%22%3A%7B%7D%7D%2C%7B%22module_name%22%3A%22supplierProductionCapacity%22%2C%22module_data%22%3A%7B%7D%7D%2C%7B%22module_name%22%3A%22supplierProductionFlow%22%2C%22module_data%22%3A%7B%7D%7D%2C%7B%22module_name%22%3A%22supplierQualityManagementProcess%22%2C%22module_data%22%3A%7B%7D%7D%2C%7B%22module_name%22%3A%22supplierProductionLineEmployee%22%2C%22module_data%22%3A%7B%7D%7D%2C%7B%22module_name%22%3A%22rd%22%2C%22module_data%22%3A%7B%7D%7D%2C%7B%22module_name%22%3A%22supplierTestReport%22%2C%22module_data%22%3A%7B%7D%7D%2C%7B%22module_name%22%3A%22supplierTradeMarket%22%2C%22module_data%22%3A%7B%7D%7D%2C%7B%22module_name%22%3A%22detailCompanyProfileFooter%22%2C%22module_data%22%3A%7B%7D%7D%5D&detailId={}'.format(id)
# browser.get(url2)
import requests
from bs4 import BeautifulSoup
reponse=requests.get(url2)
# print(reponse.text)
soup=BeautifulSoup(reponse.text,'lxml')
a=soup.select('tbody .odd')
b=soup.select('tbody .even')
c=soup.select('tbody')
import re

print(c)
p=re.compile('<tr.*?"(odd|even)">.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?</tr>',re.S)
DDDD=p.findall(str(c))
market = {}
for dic in DDDD:
    print(dic[1].replace(' ',''),dic[2])
    market[dic[1].replace(' ','')]=dic[2]
# print(a,b)
print(market)
# data = {}
# data['data'] = [{"module_name": "supplierBasicInformation", "module_data": {}},
#                 {"module_name": "supplierAndProductSamples", "module_data": {}},
#                 {"module_name": "supplierProductionCapacity", "module_data": {}},
#                 {"module_name": "supplierProductionFlow", "module_data": {}},
#                 {"module_name": "supplierQualityManagementProcess", "module_data": {}},
#                 {"module_name": "supplierProductionLineEmployee", "module_data": {}},
#                 {"module_name": "rd", "module_data": {}}, {"module_name": "supplierTestReport", "module_data": {}},
#                 {"module_name": "supplierTradeMarket", "module_data": {}},
#                 {"module_name": "detailCompanyProfileFooter", "module_data": {}}]
# data['detailId'] = 60451064794
#
# browser.get(url2)
# #############################滚动操作
# s = 'window.scrollTo({}, {})'
# i = '0'
# m = 40
# j = m
# while j > 0:
#     # k = '(document.body.scrollHeight) / {}'.format(str(j))
#     k = '(document.body.scrollHeight)/{}*{}'.format(str(m), str(j))
#     browser.execute_script(s.format(i, k))
#     i = k
#     j -= 1
# i0 = 'document.body.scrollHeight'
# j = 1
# while j <= m:
#     # k = '(document.body.scrollHeight) / {}'.format(str(j))
#     k = '(document.body.scrollHeight)/{}*{}'.format(str(m), str(j))
#     browser.execute_script(s.format(i0, k))
#     i0 = k
#     j += 1
# import time
#
# time.sleep(1)
# ##############################
#
# # spider.browser.execute_script(
# #     'var i=1000;while(i>0){window.scrollTo(0, (document.body.scrollHeight)/i)}')
#
# # 鼠标下滑加载
# # for i in range(3): #下滑三次
# #     spider.browser.execute_script('window.scrollTo(0,document.body.scrollHeight);var leftOfPage = document.body.scrollHeight;return leftOfPage;') #执行js代码
# #     time.sleep(2)
# from selenium.webdriver.support import expected_conditions as EC
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
#
# # locator1=(By.CSS_SELECTOR,'.item-content')
# locator2 = (By.CSS_SELECTOR, 'img')
# locator3 = (By.CSS_SELECTOR, 'div')
# locator4 = (By.CSS_SELECTOR, 'span')
#
# # locator=(By.CSS_SELECTOR,'h2')
# # locator4=(By.CSS_SELECTOR,'.kv')
# # WebDriverWait(spider.browser, 20, 0.5).until(EC.presence_of_all_elements_located(locator))
# # WebDriverWait(spider.browser, 20, 0.5).until(EC.presence_of_all_elements_located(locator1))
# WebDriverWait(browser, 20, 0.5).until(EC.presence_of_all_elements_located(locator2))
# WebDriverWait(browser, 20, 0.5).until(EC.presence_of_all_elements_located(locator3))
# WebDriverWait(browser, 20, 0.5).until(EC.presence_of_all_elements_located(locator4))
#
# # button = browser.find_element_by_css_selector(' div.next-tabs-bar > div > div > div > div > div:nth-child(2)')
#
# # print(button)
# # '#J-ls-grid-desc > div.detail-box.box-type-detailTab > div > div.tab-main > div > div.next-tabs-bar > div > div > div > div > div.nexd'
# # button.click() # 点击按钮
