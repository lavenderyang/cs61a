(function(){/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var n;function aa(a){var b=0;return function(){return b<a.length?{done:!1,value:a[b++]}:{done:!0}}}
var ba="function"==typeof Object.defineProperties?Object.defineProperty:function(a,b,c){if(a==Array.prototype||a==Object.prototype)return a;a[b]=c.value;return a};
function ca(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("Cannot find global object");}
var da=ca(this);function t(a,b){if(b)a:{for(var c=da,d=a.split("."),e=0;e<d.length-1;e++){var f=d[e];if(!(f in c))break a;c=c[f]}d=d[d.length-1];e=c[d];f=b(e);f!=e&&null!=f&&ba(c,d,{configurable:!0,writable:!0,value:f})}}
t("Symbol",function(a){function b(e){if(this instanceof b)throw new TypeError("Symbol is not a constructor");return new c("jscomp_symbol_"+(e||"")+"_"+d++,e)}
function c(e,f){this.f=e;ba(this,"description",{configurable:!0,writable:!0,value:f})}
if(a)return a;c.prototype.toString=function(){return this.f};
var d=0;return b});
t("Symbol.iterator",function(a){if(a)return a;a=Symbol("Symbol.iterator");for(var b="Array Int8Array Uint8Array Uint8ClampedArray Int16Array Uint16Array Int32Array Uint32Array Float32Array Float64Array".split(" "),c=0;c<b.length;c++){var d=da[b[c]];"function"===typeof d&&"function"!=typeof d.prototype[a]&&ba(d.prototype,a,{configurable:!0,writable:!0,value:function(){return ea(aa(this))}})}return a});
function ea(a){a={next:a};a[Symbol.iterator]=function(){return this};
return a}
function u(a){var b="undefined"!=typeof Symbol&&Symbol.iterator&&a[Symbol.iterator];return b?b.call(a):{next:aa(a)}}
function fa(a){for(var b,c=[];!(b=a.next()).done;)c.push(b.value);return c}
var ha="function"==typeof Object.create?Object.create:function(a){function b(){}
b.prototype=a;return new b},ia=function(){function a(){function c(){}
new c;Reflect.construct(c,[],function(){});
return new c instanceof c}
if("undefined"!=typeof Reflect&&Reflect.construct){if(a())return Reflect.construct;var b=Reflect.construct;return function(c,d,e){c=b(c,d);e&&Reflect.setPrototypeOf(c,e.prototype);return c}}return function(c,d,e){void 0===e&&(e=c);
e=ha(e.prototype||Object.prototype);return Function.prototype.apply.call(c,e,d)||e}}(),ja;
if("function"==typeof Object.setPrototypeOf)ja=Object.setPrototypeOf;else{var ka;a:{var la={a:!0},ma={};try{ma.__proto__=la;ka=ma.a;break a}catch(a){}ka=!1}ja=ka?function(a,b){a.__proto__=b;if(a.__proto__!==b)throw new TypeError(a+" is not extensible");return a}:null}var na=ja;
function v(a,b){a.prototype=ha(b.prototype);a.prototype.constructor=a;if(na)na(a,b);else for(var c in b)if("prototype"!=c)if(Object.defineProperties){var d=Object.getOwnPropertyDescriptor(b,c);d&&Object.defineProperty(a,c,d)}else a[c]=b[c];a.N=b.prototype}
function oa(){this.m=!1;this.i=null;this.g=void 0;this.f=1;this.j=this.l=0;this.u=this.h=null}
function pa(a){if(a.m)throw new TypeError("Generator is already running");a.m=!0}
oa.prototype.B=function(a){this.g=a};
function qa(a,b){a.h={Ea:b,qa:!0};a.f=a.l||a.j}
oa.prototype["return"]=function(a){this.h={"return":a};this.f=this.j};
function w(a,b,c){a.f=c;return{value:b}}
oa.prototype.H=function(a){this.f=a};
function ra(a){a.l=2;a.j=3}
function sa(a){a.l=0;a.h=null}
function ta(a){a.u=[a.h];a.l=0;a.j=0}
function ua(a){var b=a.u.splice(0)[0];(b=a.h=a.h||b)?b.qa?a.f=a.l||a.j:void 0!=b.H&&a.j<b.H?(a.f=b.H,a.h=null):a.f=a.j:a.f=0}
function va(a){this.f=new oa;this.g=a}
function wa(a,b){pa(a.f);var c=a.f.i;if(c)return xa(a,"return"in c?c["return"]:function(d){return{value:d,done:!0}},b,a.f["return"]);
a.f["return"](b);return ya(a)}
function xa(a,b,c,d){try{var e=b.call(a.f.i,c);if(!(e instanceof Object))throw new TypeError("Iterator result "+e+" is not an object");if(!e.done)return a.f.m=!1,e;var f=e.value}catch(g){return a.f.i=null,qa(a.f,g),ya(a)}a.f.i=null;d.call(a.f,f);return ya(a)}
function ya(a){for(;a.f.f;)try{var b=a.g(a.f);if(b)return a.f.m=!1,{value:b.value,done:!1}}catch(c){a.f.g=void 0,qa(a.f,c)}a.f.m=!1;if(a.f.h){b=a.f.h;a.f.h=null;if(b.qa)throw b.Ea;return{value:b["return"],done:!0}}return{value:void 0,done:!0}}
function za(a){this.next=function(b){pa(a.f);a.f.i?b=xa(a,a.f.i.next,b,a.f.B):(a.f.B(b),b=ya(a));return b};
this["throw"]=function(b){pa(a.f);a.f.i?b=xa(a,a.f.i["throw"],b,a.f.B):(qa(a.f,b),b=ya(a));return b};
this["return"]=function(b){return wa(a,b)};
this[Symbol.iterator]=function(){return this}}
function x(a,b){var c=new za(new va(b));na&&a.prototype&&na(c,a.prototype);return c}
t("Reflect",function(a){return a?a:{}});
t("Reflect.construct",function(){return ia});
t("Reflect.setPrototypeOf",function(a){return a?a:na?function(b,c){try{return na(b,c),!0}catch(d){return!1}}:null});
function Aa(a,b,c){if(null==a)throw new TypeError("The 'this' value for String.prototype."+c+" must not be null or undefined");if(b instanceof RegExp)throw new TypeError("First argument to String.prototype."+c+" must not be a regular expression");return a+""}
t("String.prototype.endsWith",function(a){return a?a:function(b,c){var d=Aa(this,b,"endsWith");b+="";void 0===c&&(c=d.length);for(var e=Math.max(0,Math.min(c|0,d.length)),f=b.length;0<f&&0<e;)if(d[--e]!=b[--f])return!1;return 0>=f}});
t("String.prototype.startsWith",function(a){return a?a:function(b,c){var d=Aa(this,b,"startsWith");b+="";for(var e=d.length,f=b.length,g=Math.max(0,Math.min(c|0,d.length)),h=0;h<f&&g<e;)if(d[g++]!=b[h++])return!1;return h>=f}});
function Ba(a,b){a instanceof String&&(a+="");var c=0,d={next:function(){if(c<a.length){var e=c++;return{value:b(e,a[e]),done:!1}}d.next=function(){return{done:!0,value:void 0}};
return d.next()}};
d[Symbol.iterator]=function(){return d};
return d}
t("Array.prototype.keys",function(a){return a?a:function(){return Ba(this,function(b){return b})}});
t("Array.prototype.values",function(a){return a?a:function(){return Ba(this,function(b,c){return c})}});
function Ca(a,b){return Object.prototype.hasOwnProperty.call(a,b)}
var Da="function"==typeof Object.assign?Object.assign:function(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(d)for(var e in d)Ca(d,e)&&(a[e]=d[e])}return a};
t("Object.assign",function(a){return a||Da});
t("Promise",function(a){function b(g){this.g=0;this.h=void 0;this.f=[];var h=this.i();try{g(h.resolve,h.reject)}catch(k){h.reject(k)}}
function c(){this.f=null}
function d(g){return g instanceof b?g:new b(function(h){h(g)})}
if(a)return a;c.prototype.g=function(g){if(null==this.f){this.f=[];var h=this;this.h(function(){h.j()})}this.f.push(g)};
var e=da.setTimeout;c.prototype.h=function(g){e(g,0)};
c.prototype.j=function(){for(;this.f&&this.f.length;){var g=this.f;this.f=[];for(var h=0;h<g.length;++h){var k=g[h];g[h]=null;try{k()}catch(l){this.i(l)}}}this.f=null};
c.prototype.i=function(g){this.h(function(){throw g;})};
b.prototype.i=function(){function g(l){return function(m){k||(k=!0,l.call(h,m))}}
var h=this,k=!1;return{resolve:g(this.C),reject:g(this.j)}};
b.prototype.C=function(g){if(g===this)this.j(new TypeError("A Promise cannot resolve to itself"));else if(g instanceof b)this.F(g);else{a:switch(typeof g){case "object":var h=null!=g;break a;case "function":h=!0;break a;default:h=!1}h?this.u(g):this.l(g)}};
b.prototype.u=function(g){var h=void 0;try{h=g.then}catch(k){this.j(k);return}"function"==typeof h?this.G(h,g):this.l(g)};
b.prototype.j=function(g){this.m(2,g)};
b.prototype.l=function(g){this.m(1,g)};
b.prototype.m=function(g,h){if(0!=this.g)throw Error("Cannot settle("+g+", "+h+"): Promise already settled in state"+this.g);this.g=g;this.h=h;this.B()};
b.prototype.B=function(){if(null!=this.f){for(var g=0;g<this.f.length;++g)f.g(this.f[g]);this.f=null}};
var f=new c;b.prototype.F=function(g){var h=this.i();g.ca(h.resolve,h.reject)};
b.prototype.G=function(g,h){var k=this.i();try{g.call(h,k.resolve,k.reject)}catch(l){k.reject(l)}};
b.prototype.then=function(g,h){function k(r,q){return"function"==typeof r?function(A){try{l(r(A))}catch(D){m(D)}}:q}
var l,m,p=new b(function(r,q){l=r;m=q});
this.ca(k(g,l),k(h,m));return p};
b.prototype["catch"]=function(g){return this.then(void 0,g)};
b.prototype.ca=function(g,h){function k(){switch(l.g){case 1:g(l.h);break;case 2:h(l.h);break;default:throw Error("Unexpected state: "+l.g);}}
var l=this;null==this.f?f.g(k):this.f.push(k)};
b.resolve=d;b.reject=function(g){return new b(function(h,k){k(g)})};
b.race=function(g){return new b(function(h,k){for(var l=u(g),m=l.next();!m.done;m=l.next())d(m.value).ca(h,k)})};
b.all=function(g){var h=u(g),k=h.next();return k.done?d([]):new b(function(l,m){function p(A){return function(D){r[A]=D;q--;0==q&&l(r)}}
var r=[],q=0;do r.push(void 0),q++,d(k.value).ca(p(r.length-1),m),k=h.next();while(!k.done)})};
return b});
t("Object.setPrototypeOf",function(a){return a||na});
t("Object.is",function(a){return a?a:function(b,c){return b===c?0!==b||1/b===1/c:b!==b&&c!==c}});
t("Array.prototype.includes",function(a){return a?a:function(b,c){var d=this;d instanceof String&&(d=String(d));var e=d.length,f=c||0;for(0>f&&(f=Math.max(f+e,0));f<e;f++){var g=d[f];if(g===b||Object.is(g,b))return!0}return!1}});
t("String.prototype.includes",function(a){return a?a:function(b,c){return-1!==Aa(this,b,"includes").indexOf(b,c||0)}});
t("WeakMap",function(a){function b(k){this.f=(h+=Math.random()+1).toString();if(k){k=u(k);for(var l;!(l=k.next()).done;)l=l.value,this.set(l[0],l[1])}}
function c(){}
function d(k){var l=typeof k;return"object"===l&&null!==k||"function"===l}
function e(k){if(!Ca(k,g)){var l=new c;ba(k,g,{value:l})}}
function f(k){var l=Object[k];l&&(Object[k]=function(m){if(m instanceof c)return m;Object.isExtensible(m)&&e(m);return l(m)})}
if(function(){if(!a||!Object.seal)return!1;try{var k=Object.seal({}),l=Object.seal({}),m=new a([[k,2],[l,3]]);if(2!=m.get(k)||3!=m.get(l))return!1;m["delete"](k);m.set(l,4);return!m.has(k)&&4==m.get(l)}catch(p){return!1}}())return a;
var g="$jscomp_hidden_"+Math.random();f("freeze");f("preventExtensions");f("seal");var h=0;b.prototype.set=function(k,l){if(!d(k))throw Error("Invalid WeakMap key");e(k);if(!Ca(k,g))throw Error("WeakMap key fail: "+k);k[g][this.f]=l;return this};
b.prototype.get=function(k){return d(k)&&Ca(k,g)?k[g][this.f]:void 0};
b.prototype.has=function(k){return d(k)&&Ca(k,g)&&Ca(k[g],this.f)};
b.prototype["delete"]=function(k){return d(k)&&Ca(k,g)&&Ca(k[g],this.f)?delete k[g][this.f]:!1};
return b});
t("Array.prototype.entries",function(a){return a?a:function(){return Ba(this,function(b,c){return[b,c]})}});
t("Map",function(a){function b(){var h={};return h.previous=h.next=h.head=h}
function c(h,k){var l=h.f;return ea(function(){if(l){for(;l.head!=h.f;)l=l.previous;for(;l.next!=l.head;)return l=l.next,{done:!1,value:k(l)};l=null}return{done:!0,value:void 0}})}
function d(h,k){var l=k&&typeof k;"object"==l||"function"==l?f.has(k)?l=f.get(k):(l=""+ ++g,f.set(k,l)):l="p_"+k;var m=h.g[l];if(m&&Ca(h.g,l))for(var p=0;p<m.length;p++){var r=m[p];if(k!==k&&r.key!==r.key||k===r.key)return{id:l,list:m,index:p,A:r}}return{id:l,list:m,index:-1,A:void 0}}
function e(h){this.g={};this.f=b();this.size=0;if(h){h=u(h);for(var k;!(k=h.next()).done;)k=k.value,this.set(k[0],k[1])}}
if(function(){if(!a||"function"!=typeof a||!a.prototype.entries||"function"!=typeof Object.seal)return!1;try{var h=Object.seal({x:4}),k=new a(u([[h,"s"]]));if("s"!=k.get(h)||1!=k.size||k.get({x:4})||k.set({x:4},"t")!=k||2!=k.size)return!1;var l=k.entries(),m=l.next();if(m.done||m.value[0]!=h||"s"!=m.value[1])return!1;m=l.next();return m.done||4!=m.value[0].x||"t"!=m.value[1]||!l.next().done?!1:!0}catch(p){return!1}}())return a;
var f=new WeakMap;e.prototype.set=function(h,k){h=0===h?0:h;var l=d(this,h);l.list||(l.list=this.g[l.id]=[]);l.A?l.A.value=k:(l.A={next:this.f,previous:this.f.previous,head:this.f,key:h,value:k},l.list.push(l.A),this.f.previous.next=l.A,this.f.previous=l.A,this.size++);return this};
e.prototype["delete"]=function(h){h=d(this,h);return h.A&&h.list?(h.list.splice(h.index,1),h.list.length||delete this.g[h.id],h.A.previous.next=h.A.next,h.A.next.previous=h.A.previous,h.A.head=null,this.size--,!0):!1};
e.prototype.clear=function(){this.g={};this.f=this.f.previous=b();this.size=0};
e.prototype.has=function(h){return!!d(this,h).A};
e.prototype.get=function(h){return(h=d(this,h).A)&&h.value};
e.prototype.entries=function(){return c(this,function(h){return[h.key,h.value]})};
e.prototype.keys=function(){return c(this,function(h){return h.key})};
e.prototype.values=function(){return c(this,function(h){return h.value})};
e.prototype.forEach=function(h,k){for(var l=this.entries(),m;!(m=l.next()).done;)m=m.value,h.call(k,m[1],m[0],this)};
e.prototype[Symbol.iterator]=e.prototype.entries;var g=0;return e});
t("Object.entries",function(a){return a?a:function(b){var c=[],d;for(d in b)Ca(b,d)&&c.push([d,b[d]]);return c}});
t("Set",function(a){function b(c){this.f=new Map;if(c){c=u(c);for(var d;!(d=c.next()).done;)this.add(d.value)}this.size=this.f.size}
if(function(){if(!a||"function"!=typeof a||!a.prototype.entries||"function"!=typeof Object.seal)return!1;try{var c=Object.seal({x:4}),d=new a(u([c]));if(!d.has(c)||1!=d.size||d.add(c)!=d||1!=d.size||d.add({x:4})!=d||2!=d.size)return!1;var e=d.entries(),f=e.next();if(f.done||f.value[0]!=c||f.value[1]!=c)return!1;f=e.next();return f.done||f.value[0]==c||4!=f.value[0].x||f.value[1]!=f.value[0]?!1:e.next().done}catch(g){return!1}}())return a;
b.prototype.add=function(c){c=0===c?0:c;this.f.set(c,c);this.size=this.f.size;return this};
b.prototype["delete"]=function(c){c=this.f["delete"](c);this.size=this.f.size;return c};
b.prototype.clear=function(){this.f.clear();this.size=0};
b.prototype.has=function(c){return this.f.has(c)};
b.prototype.entries=function(){return this.f.entries()};
b.prototype.values=function(){return this.f.values()};
b.prototype.keys=b.prototype.values;b.prototype[Symbol.iterator]=b.prototype.values;b.prototype.forEach=function(c,d){var e=this;this.f.forEach(function(f){return c.call(d,f,f,e)})};
return b});
var y=this||self;function z(a,b,c){a=a.split(".");c=c||y;a[0]in c||"undefined"==typeof c.execScript||c.execScript("var "+a[0]);for(var d;a.length&&(d=a.shift());)a.length||void 0===b?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b}
var Ea=/^[\w+/_-]+[=]{0,2}$/,Fa=null;function Ga(a){return(a=a.querySelector&&a.querySelector("script[nonce]"))&&(a=a.nonce||a.getAttribute("nonce"))&&Ea.test(a)?a:""}
function B(a,b){for(var c=a.split("."),d=b||y,e=0;e<c.length;e++)if(d=d[c[e]],null==d)return null;return d}
function Ha(){}
function Ia(a){a.ka=void 0;a.getInstance=function(){return a.ka?a.ka:a.ka=new a}}
function Ja(a){var b=typeof a;return"object"!=b?b:a?Array.isArray(a)?"array":b:"null"}
function Ka(a){var b=Ja(a);return"array"==b||"object"==b&&"number"==typeof a.length}
function La(a){return"function"==Ja(a)}
function Ma(a){var b=typeof a;return"object"==b&&null!=a||"function"==b}
function Na(a){return Object.prototype.hasOwnProperty.call(a,Oa)&&a[Oa]||(a[Oa]=++Pa)}
var Oa="closure_uid_"+(1E9*Math.random()>>>0),Pa=0;function Qa(a,b,c){return a.call.apply(a.bind,arguments)}
function Ra(a,b,c){if(!a)throw Error();if(2<arguments.length){var d=Array.prototype.slice.call(arguments,2);return function(){var e=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(e,d);return a.apply(b,e)}}return function(){return a.apply(b,arguments)}}
function C(a,b,c){Function.prototype.bind&&-1!=Function.prototype.bind.toString().indexOf("native code")?C=Qa:C=Ra;return C.apply(null,arguments)}
function Sa(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}}
var E=Date.now;function Ta(a,b){z(a,b,void 0)}
function F(a,b){function c(){}
c.prototype=b.prototype;a.N=b.prototype;a.prototype=new c;a.prototype.constructor=a}
function Ua(a){return a}
;function G(a){if(Error.captureStackTrace)Error.captureStackTrace(this,G);else{var b=Error().stack;b&&(this.stack=b)}a&&(this.message=String(a))}
F(G,Error);G.prototype.name="CustomError";function Va(a){a=a.url;var b=/[?&]dsh=1(&|$)/.test(a);this.h=!b&&/[?&]ae=1(&|$)/.test(a);this.i=!b&&/[?&]ae=2(&|$)/.test(a);if((this.f=/[?&]adurl=([^&]*)/.exec(a))&&this.f[1]){try{var c=decodeURIComponent(this.f[1])}catch(d){c=null}this.g=c}}
;function Xa(a){var b=!1,c;return function(){b||(c=a(),b=!0);return c}}
;var Ya=Array.prototype.indexOf?function(a,b){return Array.prototype.indexOf.call(a,b,void 0)}:function(a,b){if("string"===typeof a)return"string"!==typeof b||1!=b.length?-1:a.indexOf(b,0);
for(var c=0;c<a.length;c++)if(c in a&&a[c]===b)return c;return-1},H=Array.prototype.forEach?function(a,b,c){Array.prototype.forEach.call(a,b,c)}:function(a,b,c){for(var d=a.length,e="string"===typeof a?a.split(""):a,f=0;f<d;f++)f in e&&b.call(c,e[f],f,a)},Za=Array.prototype.filter?function(a,b){return Array.prototype.filter.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=[],e=0,f="string"===typeof a?a.split(""):a,g=0;g<c;g++)if(g in f){var h=f[g];
b.call(void 0,h,g,a)&&(d[e++]=h)}return d},$a=Array.prototype.map?function(a,b){return Array.prototype.map.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=Array(c),e="string"===typeof a?a.split(""):a,f=0;f<c;f++)f in e&&(d[f]=b.call(void 0,e[f],f,a));
return d},ab=Array.prototype.reduce?function(a,b,c){return Array.prototype.reduce.call(a,b,c)}:function(a,b,c){var d=c;
H(a,function(e,f){d=b.call(void 0,d,e,f,a)});
return d};
function bb(a,b){a:{var c=a.length;for(var d="string"===typeof a?a.split(""):a,e=0;e<c;e++)if(e in d&&b.call(void 0,d[e],e,a)){c=e;break a}c=-1}return 0>c?null:"string"===typeof a?a.charAt(c):a[c]}
function cb(a,b){var c=Ya(a,b);0<=c&&Array.prototype.splice.call(a,c,1)}
function db(a){var b=a.length;if(0<b){for(var c=Array(b),d=0;d<b;d++)c[d]=a[d];return c}return[]}
function eb(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(Ka(d)){var e=a.length||0,f=d.length||0;a.length=e+f;for(var g=0;g<f;g++)a[e+g]=d[g]}else a.push(d)}}
;function fb(a,b){for(var c in a)b.call(void 0,a[c],c,a)}
function gb(a,b){var c=Ka(b),d=c?b:arguments;for(c=c?0:1;c<d.length;c++){if(null==a)return;a=a[d[c]]}return a}
function hb(a){var b=ib,c;for(c in b)if(a.call(void 0,b[c],c,b))return c}
function jb(a){for(var b in a)return!1;return!0}
function kb(a,b){if(null!==a&&b in a)throw Error('The object already contains the key "'+b+'"');a[b]=!0}
function lb(a,b){for(var c in a)if(!(c in b)||a[c]!==b[c])return!1;for(var d in b)if(!(d in a))return!1;return!0}
function mb(a){var b={},c;for(c in a)b[c]=a[c];return b}
function nb(a){var b=Ja(a);if("object"==b||"array"==b){if(La(a.clone))return a.clone();b="array"==b?[]:{};for(var c in a)b[c]=nb(a[c]);return b}return a}
var ob="constructor hasOwnProperty isPrototypeOf propertyIsEnumerable toLocaleString toString valueOf".split(" ");function pb(a,b){for(var c,d,e=1;e<arguments.length;e++){d=arguments[e];for(c in d)a[c]=d[c];for(var f=0;f<ob.length;f++)c=ob[f],Object.prototype.hasOwnProperty.call(d,c)&&(a[c]=d[c])}}
;var qb;function rb(){if(void 0===qb){var a=null,b=y.trustedTypes;if(b&&b.createPolicy){try{a=b.createPolicy("goog#html",{createHTML:Ua,createScript:Ua,createScriptURL:Ua})}catch(c){y.console&&y.console.error(c.message)}qb=a}else qb=a}return qb}
;function sb(a,b){this.f=a===tb&&b||"";this.g=ub}
sb.prototype.M=!0;sb.prototype.L=function(){return this.f.toString()};
sb.prototype.ja=!0;sb.prototype.ga=function(){return 1};
function vb(a){if(a instanceof sb&&a.constructor===sb&&a.g===ub)return a.f;Ja(a);return"type_error:TrustedResourceUrl"}
var ub={},tb={};var wb=String.prototype.trim?function(a){return a.trim()}:function(a){return/^[\s\xa0]*([\s\S]*?)[\s\xa0]*$/.exec(a)[1]};
function xb(a,b){if(b)a=a.replace(yb,"&amp;").replace(zb,"&lt;").replace(Ab,"&gt;").replace(Bb,"&quot;").replace(Cb,"&#39;").replace(Db,"&#0;");else{if(!Eb.test(a))return a;-1!=a.indexOf("&")&&(a=a.replace(yb,"&amp;"));-1!=a.indexOf("<")&&(a=a.replace(zb,"&lt;"));-1!=a.indexOf(">")&&(a=a.replace(Ab,"&gt;"));-1!=a.indexOf('"')&&(a=a.replace(Bb,"&quot;"));-1!=a.indexOf("'")&&(a=a.replace(Cb,"&#39;"));-1!=a.indexOf("\x00")&&(a=a.replace(Db,"&#0;"))}return a}
var yb=/&/g,zb=/</g,Ab=/>/g,Bb=/"/g,Cb=/'/g,Db=/\x00/g,Eb=/[\x00&<>"']/;function I(a,b){this.f=a===Fb&&b||"";this.g=Gb}
I.prototype.M=!0;I.prototype.L=function(){return this.f.toString()};
I.prototype.ja=!0;I.prototype.ga=function(){return 1};
function Hb(a){if(a instanceof I&&a.constructor===I&&a.g===Gb)return a.f;Ja(a);return"type_error:SafeUrl"}
var Ib=/^(?:audio\/(?:3gpp2|3gpp|aac|L16|midi|mp3|mp4|mpeg|oga|ogg|opus|x-m4a|x-matroska|x-wav|wav|webm)|font\/\w+|image\/(?:bmp|gif|jpeg|jpg|png|tiff|webp|x-icon)|text\/csv|video\/(?:mpeg|mp4|ogg|webm|quicktime|x-matroska))(?:;\w+=(?:\w+|"[\w;,= ]+"))*$/i,Jb=/^data:(.*);base64,[a-z0-9+\/]+=*$/i,Kb=/^(?:(?:https?|mailto|ftp):|[^:/?#]*(?:[/?#]|$))/i;function Lb(a){if(a instanceof I)return a;a="object"==typeof a&&a.M?a.L():String(a);Kb.test(a)||(a="about:invalid#zClosurez");return new I(Fb,a)}
var Gb={},Mb=new I(Fb,"about:invalid#zClosurez"),Fb={};var Nb;a:{var Ob=y.navigator;if(Ob){var Pb=Ob.userAgent;if(Pb){Nb=Pb;break a}}Nb=""}function J(a){return-1!=Nb.indexOf(a)}
;function Qb(){this.f="";this.h=Rb;this.g=null}
Qb.prototype.ja=!0;Qb.prototype.ga=function(){return this.g};
Qb.prototype.M=!0;Qb.prototype.L=function(){return this.f.toString()};
var Rb={};function Sb(a,b){var c=new Qb,d=rb();c.f=d?d.createHTML(a):a;c.g=b;return c}
;function Tb(a,b){var c=b instanceof I?b:Lb(b);a.href=Hb(c)}
function Ub(a,b){a.src=vb(b);var c;(c=a.ownerDocument&&a.ownerDocument.defaultView)&&c!=y?c=Ga(c.document):(null===Fa&&(Fa=Ga(y.document)),c=Fa);c&&a.setAttribute("nonce",c)}
;function Vb(a){return a=xb(a,void 0)}
function Xb(a){for(var b=0,c=0;c<a.length;++c)b=31*b+a.charCodeAt(c)>>>0;return b}
;var Yb=/^(?:([^:/?#.]+):)?(?:\/\/(?:([^\\/?#]*)@)?([^\\/?#]*?)(?::([0-9]+))?(?=[\\/?#]|$))?([^?#]+)?(?:\?([^#]*))?(?:#([\s\S]*))?$/;function Zb(a){return a?decodeURI(a):a}
function K(a){return Zb(a.match(Yb)[3]||null)}
function $b(a,b,c){if(Array.isArray(b))for(var d=0;d<b.length;d++)$b(a,String(b[d]),c);else null!=b&&c.push(a+(""===b?"":"="+encodeURIComponent(String(b))))}
function ac(a){var b=[],c;for(c in a)$b(c,a[c],b);return b.join("&")}
function bc(a,b){var c=ac(b);if(c){var d=a.indexOf("#");0>d&&(d=a.length);var e=a.indexOf("?");if(0>e||e>d){e=d;var f=""}else f=a.substring(e+1,d);d=[a.substr(0,e),f,a.substr(d)];e=d[1];d[1]=c?e?e+"&"+c:c:e;c=d[0]+(d[1]?"?"+d[1]:"")+d[2]}else c=a;return c}
var cc=/#|$/;var dc=J("Opera"),ec=J("Trident")||J("MSIE"),fc=J("Edge"),gc=J("Gecko")&&!(-1!=Nb.toLowerCase().indexOf("webkit")&&!J("Edge"))&&!(J("Trident")||J("MSIE"))&&!J("Edge"),hc=-1!=Nb.toLowerCase().indexOf("webkit")&&!J("Edge");function ic(){var a=y.document;return a?a.documentMode:void 0}
var jc;a:{var kc="",lc=function(){var a=Nb;if(gc)return/rv:([^\);]+)(\)|;)/.exec(a);if(fc)return/Edge\/([\d\.]+)/.exec(a);if(ec)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a);if(hc)return/WebKit\/(\S+)/.exec(a);if(dc)return/(?:Version)[ \/]?(\S+)/.exec(a)}();
lc&&(kc=lc?lc[1]:"");if(ec){var mc=ic();if(null!=mc&&mc>parseFloat(kc)){jc=String(mc);break a}}jc=kc}var nc=jc,oc;if(y.document&&ec){var pc=ic();oc=pc?pc:parseInt(nc,10)||void 0}else oc=void 0;var qc=oc;var rc=J("iPhone")&&!J("iPod")&&!J("iPad")||J("iPod"),sc=J("iPad");var tc={},uc=null;var L=window;function vc(a){var b=B("window.location.href");null==a&&(a='Unknown Error of type "null/undefined"');if("string"===typeof a)return{message:a,name:"Unknown error",lineNumber:"Not available",fileName:b,stack:"Not available"};var c=!1;try{var d=a.lineNumber||a.line||"Not available"}catch(g){d="Not available",c=!0}try{var e=a.fileName||a.filename||a.sourceURL||y.$googDebugFname||b}catch(g){e="Not available",c=!0}b=wc(a);if(!(!c&&a.lineNumber&&a.fileName&&a.stack&&a.message&&a.name)){c=a.message;if(null==
c){if(a.constructor&&a.constructor instanceof Function){if(a.constructor.name)c=a.constructor.name;else if(c=a.constructor,xc[c])c=xc[c];else{c=String(c);if(!xc[c]){var f=/function\s+([^\(]+)/m.exec(c);xc[c]=f?f[1]:"[Anonymous]"}c=xc[c]}c='Unknown Error of type "'+c+'"'}else c="Unknown Error of unknown type";"function"===typeof a.toString&&Object.prototype.toString!==a.toString&&(c+=": "+a.toString())}return{message:c,name:a.name||"UnknownError",lineNumber:d,fileName:e,stack:b||"Not available"}}a.stack=
b;return a}
function wc(a,b){b||(b={});b[yc(a)]=!0;var c=a.stack||"",d=a.vb;d&&!b[yc(d)]&&(c+="\nCaused by: ",d.stack&&0==d.stack.indexOf(d.toString())||(c+="string"===typeof d?d:d.message+"\n"),c+=wc(d,b));return c}
function yc(a){var b="";"function"===typeof a.toString&&(b=""+a);return b+a.stack}
var xc={};function zc(a){this.f=a||{cookie:""}}
n=zc.prototype;n.isEnabled=function(){return navigator.cookieEnabled};
n.set=function(a,b,c){var d=!1;if("object"===typeof c){var e=c.Bb;d=c.secure||!1;var f=c.domain||void 0;var g=c.path||void 0;var h=c.ra}if(/[;=\s]/.test(a))throw Error('Invalid cookie name "'+a+'"');if(/[;\r\n]/.test(b))throw Error('Invalid cookie value "'+b+'"');void 0===h&&(h=-1);c=f?";domain="+f:"";g=g?";path="+g:"";d=d?";secure":"";h=0>h?"":0==h?";expires="+(new Date(1970,1,1)).toUTCString():";expires="+(new Date(E()+1E3*h)).toUTCString();this.f.cookie=a+"="+b+c+g+h+d+(null!=e?";samesite="+e:
"")};
n.get=function(a,b){for(var c=a+"=",d=(this.f.cookie||"").split(";"),e=0,f;e<d.length;e++){f=wb(d[e]);if(0==f.lastIndexOf(c,0))return f.substr(c.length);if(f==a)return""}return b};
n.remove=function(a,b,c){var d=void 0!==this.get(a);this.set(a,"",{ra:0,path:b,domain:c});return d};
n.isEmpty=function(){return!this.f.cookie};
n.clear=function(){for(var a=(this.f.cookie||"").split(";"),b=[],c=[],d,e,f=0;f<a.length;f++)e=wb(a[f]),d=e.indexOf("="),-1==d?(b.push(""),c.push(e)):(b.push(e.substring(0,d)),c.push(e.substring(d+1)));for(a=b.length-1;0<=a;a--)this.remove(b[a])};
var Ac=new zc("undefined"==typeof document?null:document);var Bc=!ec||9<=Number(qc);function Cc(a,b){this.x=void 0!==a?a:0;this.y=void 0!==b?b:0}
n=Cc.prototype;n.clone=function(){return new Cc(this.x,this.y)};
n.equals=function(a){return a instanceof Cc&&(this==a?!0:this&&a?this.x==a.x&&this.y==a.y:!1)};
n.ceil=function(){this.x=Math.ceil(this.x);this.y=Math.ceil(this.y);return this};
n.floor=function(){this.x=Math.floor(this.x);this.y=Math.floor(this.y);return this};
n.round=function(){this.x=Math.round(this.x);this.y=Math.round(this.y);return this};function Dc(a,b){this.width=a;this.height=b}
n=Dc.prototype;n.clone=function(){return new Dc(this.width,this.height)};
n.aspectRatio=function(){return this.width/this.height};
n.isEmpty=function(){return!(this.width*this.height)};
n.ceil=function(){this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};
n.floor=function(){this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};
n.round=function(){this.width=Math.round(this.width);this.height=Math.round(this.height);return this};function Ec(a){var b=document;return"string"===typeof a?b.getElementById(a):a}
function Fc(a,b){fb(b,function(c,d){c&&"object"==typeof c&&c.M&&(c=c.L());"style"==d?a.style.cssText=c:"class"==d?a.className=c:"for"==d?a.htmlFor=c:Gc.hasOwnProperty(d)?a.setAttribute(Gc[d],c):0==d.lastIndexOf("aria-",0)||0==d.lastIndexOf("data-",0)?a.setAttribute(d,c):a[d]=c})}
var Gc={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",nonce:"nonce",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"};
function Hc(a,b,c){var d=arguments,e=document,f=String(d[0]),g=d[1];if(!Bc&&g&&(g.name||g.type)){f=["<",f];g.name&&f.push(' name="',Vb(g.name),'"');if(g.type){f.push(' type="',Vb(g.type),'"');var h={};pb(h,g);delete h.type;g=h}f.push(">");f=f.join("")}f=Ic(e,f);g&&("string"===typeof g?f.className=g:Array.isArray(g)?f.className=g.join(" "):Fc(f,g));2<d.length&&Jc(e,f,d);return f}
function Jc(a,b,c){function d(g){g&&b.appendChild("string"===typeof g?a.createTextNode(g):g)}
for(var e=2;e<c.length;e++){var f=c[e];!Ka(f)||Ma(f)&&0<f.nodeType?d(f):H(Kc(f)?db(f):f,d)}}
function Ic(a,b){b=String(b);"application/xhtml+xml"===a.contentType&&(b=b.toLowerCase());return a.createElement(b)}
function Kc(a){if(a&&"number"==typeof a.length){if(Ma(a))return"function"==typeof a.item||"string"==typeof a.item;if(La(a))return"function"==typeof a.item}return!1}
function Lc(a,b){for(var c=0;a;){if(b(a))return a;a=a.parentNode;c++}return null}
;function Mc(a){Nc();var b=rb();a=b?b.createScriptURL(a):a;return new sb(tb,a)}
var Nc=Ha;function Oc(a){var b=Pc;if(b)for(var c in b)Object.prototype.hasOwnProperty.call(b,c)&&a.call(void 0,b[c],c,b)}
function Qc(){var a=[];Oc(function(b){a.push(b)});
return a}
var Pc={ib:"allow-forms",jb:"allow-modals",kb:"allow-orientation-lock",lb:"allow-pointer-lock",mb:"allow-popups",nb:"allow-popups-to-escape-sandbox",ob:"allow-presentation",pb:"allow-same-origin",qb:"allow-scripts",rb:"allow-top-navigation",sb:"allow-top-navigation-by-user-activation"},Rc=Xa(function(){return Qc()});
function Sc(){var a=Ic(document,"IFRAME"),b={};H(Rc(),function(c){a.sandbox&&a.sandbox.supports&&a.sandbox.supports(c)&&(b[c]=!0)});
return b}
;function M(){this.g=this.g;this.B=this.B}
M.prototype.g=!1;M.prototype.dispose=function(){this.g||(this.g=!0,this.o())};
function Tc(a,b){a.g?b():(a.B||(a.B=[]),a.B.push(b))}
M.prototype.o=function(){if(this.B)for(;this.B.length;)this.B.shift()()};
function Uc(a){a&&"function"==typeof a.dispose&&a.dispose()}
function Vc(a){for(var b=0,c=arguments.length;b<c;++b){var d=arguments[b];Ka(d)?Vc.apply(null,d):Uc(d)}}
;function N(a,b){var c=void 0;return new (c||(c=Promise))(function(d,e){function f(k){try{h(b.next(k))}catch(l){e(l)}}
function g(k){try{h(b["throw"](k))}catch(l){e(l)}}
function h(k){k.done?d(k.value):(new c(function(l){l(k.value)})).then(f,g)}
h((b=b.apply(a,void 0)).next())})}
;var Wc={};function Xc(){}
function Yc(a,b){if(b!==Wc)throw Error("Bad secret");this.f=a}
v(Yc,Xc);Yc.prototype.toString=function(){return this.f};new Yc("about:blank",Wc);new Yc("about:invalid#zTSz",Wc);function Zc(a){"number"==typeof a&&(a=Math.round(a)+"px");return a}
;var $c=(new Date).getTime();function ad(a){if(!a)return"";a=a.split("#")[0].split("?")[0];a=a.toLowerCase();0==a.indexOf("//")&&(a=window.location.protocol+a);/^[\w\-]*:\/\//.test(a)||(a=window.location.href);var b=a.substring(a.indexOf("://")+3),c=b.indexOf("/");-1!=c&&(b=b.substring(0,c));a=a.substring(0,a.indexOf("://"));if("http"!==a&&"https"!==a&&"chrome-extension"!==a&&"file"!==a&&"android-app"!==a&&"chrome-search"!==a&&"chrome-untrusted"!==a&&"chrome"!==a&&"app"!==a&&"devtools"!==a)throw Error("Invalid URI scheme in origin: "+
a);c="";var d=b.indexOf(":");if(-1!=d){var e=b.substring(d+1);b=b.substring(0,d);if("http"===a&&"80"!==e||"https"===a&&"443"!==e)c=":"+e}return a+"://"+b+c}
;function bd(){function a(){e[0]=1732584193;e[1]=4023233417;e[2]=2562383102;e[3]=271733878;e[4]=3285377520;m=l=0}
function b(p){for(var r=g,q=0;64>q;q+=4)r[q/4]=p[q]<<24|p[q+1]<<16|p[q+2]<<8|p[q+3];for(q=16;80>q;q++)p=r[q-3]^r[q-8]^r[q-14]^r[q-16],r[q]=(p<<1|p>>>31)&4294967295;p=e[0];var A=e[1],D=e[2],U=e[3],id=e[4];for(q=0;80>q;q++){if(40>q)if(20>q){var Wa=U^A&(D^U);var Wb=1518500249}else Wa=A^D^U,Wb=1859775393;else 60>q?(Wa=A&D|U&(A|D),Wb=2400959708):(Wa=A^D^U,Wb=3395469782);Wa=((p<<5|p>>>27)&4294967295)+Wa+id+Wb+r[q]&4294967295;id=U;U=D;D=(A<<30|A>>>2)&4294967295;A=p;p=Wa}e[0]=e[0]+p&4294967295;e[1]=e[1]+
A&4294967295;e[2]=e[2]+D&4294967295;e[3]=e[3]+U&4294967295;e[4]=e[4]+id&4294967295}
function c(p,r){if("string"===typeof p){p=unescape(encodeURIComponent(p));for(var q=[],A=0,D=p.length;A<D;++A)q.push(p.charCodeAt(A));p=q}r||(r=p.length);q=0;if(0==l)for(;q+64<r;)b(p.slice(q,q+64)),q+=64,m+=64;for(;q<r;)if(f[l++]=p[q++],m++,64==l)for(l=0,b(f);q+64<r;)b(p.slice(q,q+64)),q+=64,m+=64}
function d(){var p=[],r=8*m;56>l?c(h,56-l):c(h,64-(l-56));for(var q=63;56<=q;q--)f[q]=r&255,r>>>=8;b(f);for(q=r=0;5>q;q++)for(var A=24;0<=A;A-=8)p[r++]=e[q]>>A&255;return p}
for(var e=[],f=[],g=[],h=[128],k=1;64>k;++k)h[k]=0;var l,m;a();return{reset:a,update:c,digest:d,Da:function(){for(var p=d(),r="",q=0;q<p.length;q++)r+="0123456789ABCDEF".charAt(Math.floor(p[q]/16))+"0123456789ABCDEF".charAt(p[q]%16);return r}}}
;function cd(a,b,c){var d=[],e=[];if(1==(Array.isArray(c)?2:1))return e=[b,a],H(d,function(h){e.push(h)}),dd(e.join(" "));
var f=[],g=[];H(c,function(h){g.push(h.key);f.push(h.value)});
c=Math.floor((new Date).getTime()/1E3);e=0==f.length?[c,b,a]:[f.join(":"),c,b,a];H(d,function(h){e.push(h)});
a=dd(e.join(" "));a=[c,a];0==g.length||a.push(g.join(""));return a.join("_")}
function dd(a){var b=bd();b.update(a);return b.Da().toLowerCase()}
;function ed(a){var b=ad(String(y.location.href)),c;(c=y.__SAPISID||y.__APISID||y.__OVERRIDE_SID)?c=!0:(c=new zc(document),c=c.get("SAPISID")||c.get("APISID")||c.get("__Secure-3PAPISID")||c.get("SID"),c=!!c);if(c&&(c=(b=0==b.indexOf("https:")||0==b.indexOf("chrome-extension:"))?y.__SAPISID:y.__APISID,c||(c=new zc(document),c=c.get(b?"SAPISID":"APISID")||c.get("__Secure-3PAPISID")),c)){b=b?"SAPISIDHASH":"APISIDHASH";var d=String(y.location.href);return d&&c&&b?[b,cd(ad(d),c,a||null)].join(" "):null}return null}
;function fd(){this.g=[];this.f=-1}
fd.prototype.set=function(a,b){b=void 0===b?!0:b;0<=a&&52>a&&0===a%1&&this.g[a]!=b&&(this.g[a]=b,this.f=-1)};
fd.prototype.get=function(a){return!!this.g[a]};
function gd(a){-1==a.f&&(a.f=ab(a.g,function(b,c,d){return c?b+Math.pow(2,d):b},0));
return a.f}
;function hd(a,b){this.h=a;this.i=b;this.g=0;this.f=null}
hd.prototype.get=function(){if(0<this.g){this.g--;var a=this.f;this.f=a.next;a.next=null}else a=this.h();return a};
function jd(a,b){a.i(b);100>a.g&&(a.g++,b.next=a.f,a.f=b)}
;function kd(a){y.setTimeout(function(){throw a;},0)}
var ld;
function md(){var a=y.MessageChannel;"undefined"===typeof a&&"undefined"!==typeof window&&window.postMessage&&window.addEventListener&&!J("Presto")&&(a=function(){var e=Ic(document,"IFRAME");e.style.display="none";document.documentElement.appendChild(e);var f=e.contentWindow;e=f.document;e.open();e.close();var g="callImmediate"+Math.random(),h="file:"==f.location.protocol?"*":f.location.protocol+"//"+f.location.host;e=C(function(k){if(("*"==h||k.origin==h)&&k.data==g)this.port1.onmessage()},this);
f.addEventListener("message",e,!1);this.port1={};this.port2={postMessage:function(){f.postMessage(g,h)}}});
if("undefined"!==typeof a&&!J("Trident")&&!J("MSIE")){var b=new a,c={},d=c;b.port1.onmessage=function(){if(void 0!==c.next){c=c.next;var e=c.oa;c.oa=null;e()}};
return function(e){d.next={oa:e};d=d.next;b.port2.postMessage(0)}}return function(e){y.setTimeout(e,0)}}
;function nd(){this.g=this.f=null}
var pd=new hd(function(){return new od},function(a){a.reset()});
nd.prototype.add=function(a,b){var c=pd.get();c.set(a,b);this.g?this.g.next=c:this.f=c;this.g=c};
nd.prototype.remove=function(){var a=null;this.f&&(a=this.f,this.f=this.f.next,this.f||(this.g=null),a.next=null);return a};
function od(){this.next=this.scope=this.f=null}
od.prototype.set=function(a,b){this.f=a;this.scope=b;this.next=null};
od.prototype.reset=function(){this.next=this.scope=this.f=null};function qd(a,b){rd||sd();td||(rd(),td=!0);ud.add(a,b)}
var rd;function sd(){if(y.Promise&&y.Promise.resolve){var a=y.Promise.resolve(void 0);rd=function(){a.then(vd)}}else rd=function(){var b=vd;
!La(y.setImmediate)||y.Window&&y.Window.prototype&&!J("Edge")&&y.Window.prototype.setImmediate==y.setImmediate?(ld||(ld=md()),ld(b)):y.setImmediate(b)}}
var td=!1,ud=new nd;function vd(){for(var a;a=ud.remove();){try{a.f.call(a.scope)}catch(b){kd(b)}jd(pd,a)}td=!1}
;function wd(){this.g=-1}
;function xd(){this.g=64;this.f=[];this.l=[];this.m=[];this.i=[];this.i[0]=128;for(var a=1;a<this.g;++a)this.i[a]=0;this.j=this.h=0;this.reset()}
F(xd,wd);xd.prototype.reset=function(){this.f[0]=1732584193;this.f[1]=4023233417;this.f[2]=2562383102;this.f[3]=271733878;this.f[4]=3285377520;this.j=this.h=0};
function yd(a,b,c){c||(c=0);var d=a.m;if("string"===typeof b)for(var e=0;16>e;e++)d[e]=b.charCodeAt(c)<<24|b.charCodeAt(c+1)<<16|b.charCodeAt(c+2)<<8|b.charCodeAt(c+3),c+=4;else for(e=0;16>e;e++)d[e]=b[c]<<24|b[c+1]<<16|b[c+2]<<8|b[c+3],c+=4;for(e=16;80>e;e++){var f=d[e-3]^d[e-8]^d[e-14]^d[e-16];d[e]=(f<<1|f>>>31)&4294967295}b=a.f[0];c=a.f[1];var g=a.f[2],h=a.f[3],k=a.f[4];for(e=0;80>e;e++){if(40>e)if(20>e){f=h^c&(g^h);var l=1518500249}else f=c^g^h,l=1859775393;else 60>e?(f=c&g|h&(c|g),l=2400959708):
(f=c^g^h,l=3395469782);f=(b<<5|b>>>27)+f+k+l+d[e]&4294967295;k=h;h=g;g=(c<<30|c>>>2)&4294967295;c=b;b=f}a.f[0]=a.f[0]+b&4294967295;a.f[1]=a.f[1]+c&4294967295;a.f[2]=a.f[2]+g&4294967295;a.f[3]=a.f[3]+h&4294967295;a.f[4]=a.f[4]+k&4294967295}
xd.prototype.update=function(a,b){if(null!=a){void 0===b&&(b=a.length);for(var c=b-this.g,d=0,e=this.l,f=this.h;d<b;){if(0==f)for(;d<=c;)yd(this,a,d),d+=this.g;if("string"===typeof a)for(;d<b;){if(e[f]=a.charCodeAt(d),++f,++d,f==this.g){yd(this,e);f=0;break}}else for(;d<b;)if(e[f]=a[d],++f,++d,f==this.g){yd(this,e);f=0;break}}this.h=f;this.j+=b}};
xd.prototype.digest=function(){var a=[],b=8*this.j;56>this.h?this.update(this.i,56-this.h):this.update(this.i,this.g-(this.h-56));for(var c=this.g-1;56<=c;c--)this.l[c]=b&255,b/=256;yd(this,this.l);for(c=b=0;5>c;c++)for(var d=24;0<=d;d-=8)a[b]=this.f[c]>>d&255,++b;return a};var zd="StopIteration"in y?y.StopIteration:{message:"StopIteration",stack:""};function Ad(){}
Ad.prototype.next=function(){throw zd;};
Ad.prototype.I=function(){return this};
function Bd(a){if(a instanceof Ad)return a;if("function"==typeof a.I)return a.I(!1);if(Ka(a)){var b=0,c=new Ad;c.next=function(){for(;;){if(b>=a.length)throw zd;if(b in a)return a[b++];b++}};
return c}throw Error("Not implemented");}
function Cd(a,b){if(Ka(a))try{H(a,b,void 0)}catch(c){if(c!==zd)throw c;}else{a=Bd(a);try{for(;;)b.call(void 0,a.next(),void 0,a)}catch(c){if(c!==zd)throw c;}}}
function Dd(a){if(Ka(a))return db(a);a=Bd(a);var b=[];Cd(a,function(c){b.push(c)});
return b}
;function Ed(a,b){this.h={};this.f=[];this.J=this.g=0;var c=arguments.length;if(1<c){if(c%2)throw Error("Uneven number of arguments");for(var d=0;d<c;d+=2)this.set(arguments[d],arguments[d+1])}else if(a)if(a instanceof Ed)for(c=Fd(a),d=0;d<c.length;d++)this.set(c[d],a.get(c[d]));else for(d in a)this.set(d,a[d])}
function Fd(a){Gd(a);return a.f.concat()}
n=Ed.prototype;n.equals=function(a,b){if(this===a)return!0;if(this.g!=a.g)return!1;var c=b||Hd;Gd(this);for(var d,e=0;d=this.f[e];e++)if(!c(this.get(d),a.get(d)))return!1;return!0};
function Hd(a,b){return a===b}
n.isEmpty=function(){return 0==this.g};
n.clear=function(){this.h={};this.J=this.g=this.f.length=0};
n.remove=function(a){return Object.prototype.hasOwnProperty.call(this.h,a)?(delete this.h[a],this.g--,this.J++,this.f.length>2*this.g&&Gd(this),!0):!1};
function Gd(a){if(a.g!=a.f.length){for(var b=0,c=0;b<a.f.length;){var d=a.f[b];Object.prototype.hasOwnProperty.call(a.h,d)&&(a.f[c++]=d);b++}a.f.length=c}if(a.g!=a.f.length){var e={};for(c=b=0;b<a.f.length;)d=a.f[b],Object.prototype.hasOwnProperty.call(e,d)||(a.f[c++]=d,e[d]=1),b++;a.f.length=c}}
n.get=function(a,b){return Object.prototype.hasOwnProperty.call(this.h,a)?this.h[a]:b};
n.set=function(a,b){Object.prototype.hasOwnProperty.call(this.h,a)||(this.g++,this.f.push(a),this.J++);this.h[a]=b};
n.forEach=function(a,b){for(var c=Fd(this),d=0;d<c.length;d++){var e=c[d],f=this.get(e);a.call(b,f,e,this)}};
n.clone=function(){return new Ed(this)};
n.I=function(a){Gd(this);var b=0,c=this.J,d=this,e=new Ad;e.next=function(){if(c!=d.J)throw Error("The map has changed since the iterator was created");if(b>=d.f.length)throw zd;var f=d.f[b++];return a?f:d.h[f]};
return e};function Id(a){return"string"==typeof a.className?a.className:a.getAttribute&&a.getAttribute("class")||""}
function Jd(a,b){"string"==typeof a.className?a.className=b:a.setAttribute&&a.setAttribute("class",b)}
function Kd(a,b){if(a.classList)var c=a.classList.contains(b);else c=a.classList?a.classList:Id(a).match(/\S+/g)||[],c=0<=Ya(c,b);return c}
function Ld(){var a=document.body;a.classList?a.classList.remove("inverted-hdpi"):Kd(a,"inverted-hdpi")&&Jd(a,Za(a.classList?a.classList:Id(a).match(/\S+/g)||[],function(b){return"inverted-hdpi"!=b}).join(" "))}
;function Md(a){var b=[];Nd(new Od,a,b);return b.join("")}
function Od(){}
function Nd(a,b,c){if(null==b)c.push("null");else{if("object"==typeof b){if(Array.isArray(b)){var d=b;b=d.length;c.push("[");for(var e="",f=0;f<b;f++)c.push(e),Nd(a,d[f],c),e=",";c.push("]");return}if(b instanceof String||b instanceof Number||b instanceof Boolean)b=b.valueOf();else{c.push("{");e="";for(d in b)Object.prototype.hasOwnProperty.call(b,d)&&(f=b[d],"function"!=typeof f&&(c.push(e),Pd(d,c),c.push(":"),Nd(a,f,c),e=","));c.push("}");return}}switch(typeof b){case "string":Pd(b,c);break;case "number":c.push(isFinite(b)&&
!isNaN(b)?String(b):"null");break;case "boolean":c.push(String(b));break;case "function":c.push("null");break;default:throw Error("Unknown type: "+typeof b);}}}
var Qd={'"':'\\"',"\\":"\\\\","/":"\\/","\b":"\\b","\f":"\\f","\n":"\\n","\r":"\\r","\t":"\\t","\x0B":"\\u000b"},Rd=/\uffff/.test("\uffff")?/[\\"\x00-\x1f\x7f-\uffff]/g:/[\\"\x00-\x1f\x7f-\xff]/g;function Pd(a,b){b.push('"',a.replace(Rd,function(c){var d=Qd[c];d||(d="\\u"+(c.charCodeAt(0)|65536).toString(16).substr(1),Qd[c]=d);return d}),'"')}
;function Sd(a){if(!a)return!1;try{return!!a.$goog_Thenable}catch(b){return!1}}
;function O(a){this.f=0;this.m=void 0;this.i=this.g=this.h=null;this.j=this.l=!1;if(a!=Ha)try{var b=this;a.call(void 0,function(c){Td(b,2,c)},function(c){Td(b,3,c)})}catch(c){Td(this,3,c)}}
function Ud(){this.next=this.context=this.onRejected=this.g=this.f=null;this.h=!1}
Ud.prototype.reset=function(){this.context=this.onRejected=this.g=this.f=null;this.h=!1};
var Vd=new hd(function(){return new Ud},function(a){a.reset()});
function Wd(a,b,c){var d=Vd.get();d.g=a;d.onRejected=b;d.context=c;return d}
function Xd(a){if(a instanceof O)return a;var b=new O(Ha);Td(b,2,a);return b}
function Yd(a){return new O(function(b,c){c(a)})}
O.prototype.then=function(a,b,c){return Zd(this,La(a)?a:null,La(b)?b:null,c)};
O.prototype.$goog_Thenable=!0;function $d(a,b){return Zd(a,null,b,void 0)}
O.prototype.cancel=function(a){if(0==this.f){var b=new ae(a);qd(function(){be(this,b)},this)}};
function be(a,b){if(0==a.f)if(a.h){var c=a.h;if(c.g){for(var d=0,e=null,f=null,g=c.g;g&&(g.h||(d++,g.f==a&&(e=g),!(e&&1<d)));g=g.next)e||(f=g);e&&(0==c.f&&1==d?be(c,b):(f?(d=f,d.next==c.i&&(c.i=d),d.next=d.next.next):ce(c),de(c,e,3,b)))}a.h=null}else Td(a,3,b)}
function ee(a,b){a.g||2!=a.f&&3!=a.f||fe(a);a.i?a.i.next=b:a.g=b;a.i=b}
function Zd(a,b,c,d){var e=Wd(null,null,null);e.f=new O(function(f,g){e.g=b?function(h){try{var k=b.call(d,h);f(k)}catch(l){g(l)}}:f;
e.onRejected=c?function(h){try{var k=c.call(d,h);void 0===k&&h instanceof ae?g(h):f(k)}catch(l){g(l)}}:g});
e.f.h=a;ee(a,e);return e.f}
O.prototype.u=function(a){this.f=0;Td(this,2,a)};
O.prototype.C=function(a){this.f=0;Td(this,3,a)};
function Td(a,b,c){if(0==a.f){a===c&&(b=3,c=new TypeError("Promise cannot resolve to itself"));a.f=1;a:{var d=c,e=a.u,f=a.C;if(d instanceof O){ee(d,Wd(e||Ha,f||null,a));var g=!0}else if(Sd(d))d.then(e,f,a),g=!0;else{if(Ma(d))try{var h=d.then;if(La(h)){ge(d,h,e,f,a);g=!0;break a}}catch(k){f.call(a,k);g=!0;break a}g=!1}}g||(a.m=c,a.f=b,a.h=null,fe(a),3!=b||c instanceof ae||he(a,c))}}
function ge(a,b,c,d,e){function f(k){h||(h=!0,d.call(e,k))}
function g(k){h||(h=!0,c.call(e,k))}
var h=!1;try{b.call(a,g,f)}catch(k){f(k)}}
function fe(a){a.l||(a.l=!0,qd(a.B,a))}
function ce(a){var b=null;a.g&&(b=a.g,a.g=b.next,b.next=null);a.g||(a.i=null);return b}
O.prototype.B=function(){for(var a;a=ce(this);)de(this,a,this.f,this.m);this.l=!1};
function de(a,b,c,d){if(3==c&&b.onRejected&&!b.h)for(;a&&a.j;a=a.h)a.j=!1;if(b.f)b.f.h=null,ie(b,c,d);else try{b.h?b.g.call(b.context):ie(b,c,d)}catch(e){je.call(null,e)}jd(Vd,b)}
function ie(a,b,c){2==b?a.g.call(a.context,c):a.onRejected&&a.onRejected.call(a.context,c)}
function he(a,b){a.j=!0;qd(function(){a.j&&je.call(null,b)})}
var je=kd;function ae(a){G.call(this,a)}
F(ae,G);ae.prototype.name="cancel";function P(a){M.call(this);this.l=1;this.i=[];this.j=0;this.f=[];this.h={};this.m=!!a}
F(P,M);n=P.prototype;n.subscribe=function(a,b,c){var d=this.h[a];d||(d=this.h[a]=[]);var e=this.l;this.f[e]=a;this.f[e+1]=b;this.f[e+2]=c;this.l=e+3;d.push(e);return e};
function ke(a,b,c,d){if(b=a.h[b]){var e=a.f;(b=bb(b,function(f){return e[f+1]==c&&e[f+2]==d}))&&a.P(b)}}
n.P=function(a){var b=this.f[a];if(b){var c=this.h[b];0!=this.j?(this.i.push(a),this.f[a+1]=Ha):(c&&cb(c,a),delete this.f[a],delete this.f[a+1],delete this.f[a+2])}return!!b};
n.O=function(a,b){var c=this.h[a];if(c){for(var d=Array(arguments.length-1),e=1,f=arguments.length;e<f;e++)d[e-1]=arguments[e];if(this.m)for(e=0;e<c.length;e++){var g=c[e];le(this.f[g+1],this.f[g+2],d)}else{this.j++;try{for(e=0,f=c.length;e<f;e++)g=c[e],this.f[g+1].apply(this.f[g+2],d)}finally{if(this.j--,0<this.i.length&&0==this.j)for(;c=this.i.pop();)this.P(c)}}return 0!=e}return!1};
function le(a,b,c){qd(function(){a.apply(b,c)})}
n.clear=function(a){if(a){var b=this.h[a];b&&(H(b,this.P,this),delete this.h[a])}else this.f.length=0,this.h={}};
n.o=function(){P.N.o.call(this);this.clear();this.i.length=0};function me(a){this.f=a}
me.prototype.set=function(a,b){void 0===b?this.f.remove(a):this.f.set(a,Md(b))};
me.prototype.get=function(a){try{var b=this.f.get(a)}catch(c){return}if(null!==b)try{return JSON.parse(b)}catch(c){throw"Storage: Invalid value was encountered";}};
me.prototype.remove=function(a){this.f.remove(a)};function ne(a){this.f=a}
F(ne,me);function oe(a){this.data=a}
function pe(a){return void 0===a||a instanceof oe?a:new oe(a)}
ne.prototype.set=function(a,b){ne.N.set.call(this,a,pe(b))};
ne.prototype.g=function(a){a=ne.N.get.call(this,a);if(void 0===a||a instanceof Object)return a;throw"Storage: Invalid value was encountered";};
ne.prototype.get=function(a){if(a=this.g(a)){if(a=a.data,void 0===a)throw"Storage: Invalid value was encountered";}else a=void 0;return a};function qe(a){this.f=a}
F(qe,ne);qe.prototype.set=function(a,b,c){if(b=pe(b)){if(c){if(c<E()){qe.prototype.remove.call(this,a);return}b.expiration=c}b.creation=E()}qe.N.set.call(this,a,b)};
qe.prototype.g=function(a){var b=qe.N.g.call(this,a);if(b){var c=b.creation,d=b.expiration;if(d&&d<E()||c&&c>E())qe.prototype.remove.call(this,a);else return b}};function re(){}
;function se(){}
F(se,re);se.prototype.clear=function(){var a=Dd(this.I(!0)),b=this;H(a,function(c){b.remove(c)})};function te(a){this.f=a}
F(te,se);n=te.prototype;n.isAvailable=function(){if(!this.f)return!1;try{return this.f.setItem("__sak","1"),this.f.removeItem("__sak"),!0}catch(a){return!1}};
n.set=function(a,b){try{this.f.setItem(a,b)}catch(c){if(0==this.f.length)throw"Storage mechanism: Storage disabled";throw"Storage mechanism: Quota exceeded";}};
n.get=function(a){a=this.f.getItem(a);if("string"!==typeof a&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
n.remove=function(a){this.f.removeItem(a)};
n.I=function(a){var b=0,c=this.f,d=new Ad;d.next=function(){if(b>=c.length)throw zd;var e=c.key(b++);if(a)return e;e=c.getItem(e);if("string"!==typeof e)throw"Storage mechanism: Invalid value was encountered";return e};
return d};
n.clear=function(){this.f.clear()};
n.key=function(a){return this.f.key(a)};function ue(){var a=null;try{a=window.localStorage||null}catch(b){}this.f=a}
F(ue,te);function ve(a,b){this.g=a;this.f=null;if(ec&&!(9<=Number(qc))){we||(we=new Ed);this.f=we.get(a);this.f||(b?this.f=document.getElementById(b):(this.f=document.createElement("userdata"),this.f.addBehavior("#default#userData"),document.body.appendChild(this.f)),we.set(a,this.f));try{this.f.load(this.g)}catch(c){this.f=null}}}
F(ve,se);var xe={".":".2E","!":".21","~":".7E","*":".2A","'":".27","(":".28",")":".29","%":"."},we=null;function ye(a){return"_"+encodeURIComponent(a).replace(/[.!~*'()%]/g,function(b){return xe[b]})}
n=ve.prototype;n.isAvailable=function(){return!!this.f};
n.set=function(a,b){this.f.setAttribute(ye(a),b);ze(this)};
n.get=function(a){a=this.f.getAttribute(ye(a));if("string"!==typeof a&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
n.remove=function(a){this.f.removeAttribute(ye(a));ze(this)};
n.I=function(a){var b=0,c=this.f.XMLDocument.documentElement.attributes,d=new Ad;d.next=function(){if(b>=c.length)throw zd;var e=c[b++];if(a)return decodeURIComponent(e.nodeName.replace(/\./g,"%")).substr(1);e=e.nodeValue;if("string"!==typeof e)throw"Storage mechanism: Invalid value was encountered";return e};
return d};
n.clear=function(){for(var a=this.f.XMLDocument.documentElement,b=a.attributes.length;0<b;b--)a.removeAttribute(a.attributes[b-1].nodeName);ze(this)};
function ze(a){try{a.f.save(a.g)}catch(b){throw"Storage mechanism: Quota exceeded";}}
;function Ae(a,b){this.g=a;this.f=b+"::"}
F(Ae,se);Ae.prototype.set=function(a,b){this.g.set(this.f+a,b)};
Ae.prototype.get=function(a){return this.g.get(this.f+a)};
Ae.prototype.remove=function(a){this.g.remove(this.f+a)};
Ae.prototype.I=function(a){var b=this.g.I(!0),c=this,d=new Ad;d.next=function(){for(var e=b.next();e.substr(0,c.f.length)!=c.f;)e=b.next();return a?e.substr(c.f.length):c.g.get(e)};
return d};function Be(a,b){1<b.length?a[b[0]]=b[1]:1===b.length&&Object.assign(a,b[0])}
;var Ce=window.yt&&window.yt.config_||window.ytcfg&&window.ytcfg.data_||{};z("yt.config_",Ce,void 0);function Q(a){Be(Ce,arguments)}
function R(a,b){return a in Ce?Ce[a]:b}
function De(){return R("PLAYER_CONFIG",{})}
;function Ee(){var a=Fe;B("yt.ads.biscotti.getId_")||z("yt.ads.biscotti.getId_",a,void 0)}
function Ge(a){z("yt.ads.biscotti.lastId_",a,void 0)}
;var He=[];function Ie(a){He.forEach(function(b){return b(a)})}
function Je(a){return a&&window.yterr?function(){try{return a.apply(this,arguments)}catch(b){S(b),Ie(b)}}:a}
function S(a){var b=B("yt.logging.errors.log");b?b(a,"ERROR",void 0,void 0,void 0):(b=R("ERRORS",[]),b.push([a,"ERROR",void 0,void 0,void 0]),Q("ERRORS",b))}
function Ke(a){var b=B("yt.logging.errors.log");b?b(a,"WARNING",void 0,void 0,void 0):(b=R("ERRORS",[]),b.push([a,"WARNING",void 0,void 0,void 0]),Q("ERRORS",b))}
;function Le(a){a=a.split("&");for(var b={},c=0,d=a.length;c<d;c++){var e=a[c].split("=");if(1==e.length&&e[0]||2==e.length)try{var f=decodeURIComponent((e[0]||"").replace(/\+/g," ")),g=decodeURIComponent((e[1]||"").replace(/\+/g," "));f in b?Array.isArray(b[f])?eb(b[f],g):b[f]=[b[f],g]:b[f]=g}catch(k){if("q"!=e[0]){var h=Error("Error decoding URL component");h.params={key:e[0],value:e[1]};S(h)}}}return b}
function Me(a){var b=[];fb(a,function(c,d){var e=encodeURIComponent(String(d)),f;Array.isArray(c)?f=c:f=[c];H(f,function(g){""==g?b.push(e):b.push(e+"="+encodeURIComponent(String(g)))})});
return b.join("&")}
function Ne(a){"?"==a.charAt(0)&&(a=a.substr(1));return Le(a)}
function Oe(a,b,c){var d=a.split("#",2);a=d[0];d=1<d.length?"#"+d[1]:"";var e=a.split("?",2);a=e[0];e=Ne(e[1]||"");for(var f in b)!c&&null!==e&&f in e||(e[f]=b[f]);return bc(a,e)+d}
;function Pe(a){var b=Qe;a=void 0===a?B("yt.ads.biscotti.lastId_")||"":a;b=Object.assign(Re(b),Se(b));b.ca_type="image";a&&(b.bid=a);return b}
function Re(a){var b={};b.dt=$c;b.flash="0";a:{try{var c=a.f.top.location.href}catch(f){a=2;break a}a=c?c===a.g.location.href?0:1:2}b=(b.frm=a,b);b.u_tz=-(new Date).getTimezoneOffset();var d=void 0===d?L:d;try{var e=d.history.length}catch(f){e=0}b.u_his=e;b.u_java=!!L.navigator&&"unknown"!==typeof L.navigator.javaEnabled&&!!L.navigator.javaEnabled&&L.navigator.javaEnabled();L.screen&&(b.u_h=L.screen.height,b.u_w=L.screen.width,b.u_ah=L.screen.availHeight,b.u_aw=L.screen.availWidth,b.u_cd=L.screen.colorDepth);
L.navigator&&L.navigator.plugins&&(b.u_nplug=L.navigator.plugins.length);L.navigator&&L.navigator.mimeTypes&&(b.u_nmime=L.navigator.mimeTypes.length);return b}
function Se(a){var b=a.f;try{var c=b.screenX;var d=b.screenY}catch(p){}try{var e=b.outerWidth;var f=b.outerHeight}catch(p){}try{var g=b.innerWidth;var h=b.innerHeight}catch(p){}b=[b.screenLeft,b.screenTop,c,d,b.screen?b.screen.availWidth:void 0,b.screen?b.screen.availTop:void 0,e,f,g,h];c=a.f.top;try{var k=(c||window).document,l="CSS1Compat"==k.compatMode?k.documentElement:k.body;var m=(new Dc(l.clientWidth,l.clientHeight)).round()}catch(p){m=new Dc(-12245933,-12245933)}k=m;m={};l=new fd;y.SVGElement&&
y.document.createElementNS&&l.set(0);c=Sc();c["allow-top-navigation-by-user-activation"]&&l.set(1);c["allow-popups-to-escape-sandbox"]&&l.set(2);y.crypto&&y.crypto.subtle&&l.set(3);y.TextDecoder&&y.TextEncoder&&l.set(4);l=gd(l);m.bc=l;m.bih=k.height;m.biw=k.width;m.brdim=b.join();a=a.g;return m.vis={visible:1,hidden:2,prerender:3,preview:4,unloaded:5}[a.visibilityState||a.webkitVisibilityState||a.mozVisibilityState||""]||0,m.wgl=!!L.WebGLRenderingContext,m}
var Qe=new function(){var a=window.document;this.f=window;this.g=a};
z("yt.ads_.signals_.getAdSignalsString",function(a){return Me(Pe(a))},void 0);E();function T(a){a=Te(a);return"string"===typeof a&&"false"===a?!1:!!a}
function Ue(a,b){var c=Te(a);return void 0===c&&void 0!==b?b:Number(c||0)}
function Te(a){var b=R("EXPERIMENTS_FORCED_FLAGS",{});return void 0!==b[a]?b[a]:R("EXPERIMENT_FLAGS",{})[a]}
;var Ve="XMLHttpRequest"in y?function(){return new XMLHttpRequest}:null;
function We(){if(!Ve)return null;var a=Ve();return"open"in a?a:null}
function Xe(a){switch(a&&"status"in a?a.status:-1){case 200:case 201:case 202:case 203:case 204:case 205:case 206:case 304:return!0;default:return!1}}
;function V(a,b){"function"===typeof a&&(a=Je(a));return window.setTimeout(a,b)}
function W(a){window.clearTimeout(a)}
;var Ye={Authorization:"AUTHORIZATION","X-Goog-Visitor-Id":"SANDBOXED_VISITOR_ID","X-YouTube-Client-Name":"INNERTUBE_CONTEXT_CLIENT_NAME","X-YouTube-Client-Version":"INNERTUBE_CONTEXT_CLIENT_VERSION","X-YouTube-Device":"DEVICE","X-Youtube-Identity-Token":"ID_TOKEN","X-YouTube-Page-CL":"PAGE_CL","X-YouTube-Page-Label":"PAGE_BUILD_LABEL","X-YouTube-Variants-Checksum":"VARIANTS_CHECKSUM"},Ze="app debugcss debugjs expflag force_ad_params force_viral_ad_response_params forced_experiments innertube_snapshots innertube_goldens internalcountrycode internalipoverride absolute_experiments conditional_experiments sbb sr_bns_address".split(" "),
$e=!1;
function af(a,b){b=void 0===b?{}:b;if(!c)var c=window.location.href;var d=a.match(Yb)[1]||null,e=K(a);d&&e?(d=c,c=a.match(Yb),d=d.match(Yb),c=c[3]==d[3]&&c[1]==d[1]&&c[4]==d[4]):c=e?K(c)==e&&(Number(c.match(Yb)[4]||null)||null)==(Number(a.match(Yb)[4]||null)||null):!0;d=T("web_ajax_ignore_global_headers_if_set");for(var f in Ye)e=R(Ye[f]),!e||!c&&K(a)||d&&void 0!==b[f]||(b[f]=e);if(c||!K(a))b["X-YouTube-Utc-Offset"]=String(-(new Date).getTimezoneOffset());(c||!K(a))&&(f="undefined"!=typeof Intl?(new Intl.DateTimeFormat).resolvedOptions().timeZone:
null)&&(b["X-YouTube-Time-Zone"]=f);if(c||!K(a))b["X-YouTube-Ad-Signals"]=Me(Pe(void 0));return b}
function bf(a){var b=window.location.search,c=K(a),d=Zb(a.match(Yb)[5]||null);d=(c=c&&(c.endsWith("youtube.com")||c.endsWith("youtube-nocookie.com")))&&d&&d.startsWith("/api/");if(!c||d)return a;var e=Ne(b),f={};H(Ze,function(g){e[g]&&(f[g]=e[g])});
return Oe(a,f||{},!1)}
function cf(a,b){if(window.fetch&&"XML"!=b.format){var c={method:b.method||"GET",credentials:"same-origin"};b.headers&&(c.headers=b.headers);a=df(a,b);var d=ef(a,b);d&&(c.body=d);b.withCredentials&&(c.credentials="include");var e=!1,f;fetch(a,c).then(function(g){if(!e){e=!0;f&&W(f);var h=g.ok,k=function(l){l=l||{};var m=b.context||y;h?b.onSuccess&&b.onSuccess.call(m,l,g):b.onError&&b.onError.call(m,l,g);b.la&&b.la.call(m,l,g)};
"JSON"==(b.format||"JSON")&&(h||400<=g.status&&500>g.status)?g.json().then(k,function(){k(null)}):k(null)}});
b.va&&0<b.timeout&&(f=V(function(){e||(e=!0,W(f),b.va.call(b.context||y))},b.timeout))}else ff(a,b)}
function ff(a,b){var c=b.format||"JSON";a=df(a,b);var d=ef(a,b),e=!1,f=gf(a,function(k){if(!e){e=!0;h&&W(h);var l=Xe(k),m=null,p=400<=k.status&&500>k.status,r=500<=k.status&&600>k.status;if(l||p||r)m=hf(a,c,k,b.wb);if(l)a:if(k&&204==k.status)l=!0;else{switch(c){case "XML":l=0==parseInt(m&&m.return_code,10);break a;case "RAW":l=!0;break a}l=!!m}m=m||{};p=b.context||y;l?b.onSuccess&&b.onSuccess.call(p,k,m):b.onError&&b.onError.call(p,k,m);b.la&&b.la.call(p,k,m)}},b.method,d,b.headers,b.responseType,
b.withCredentials);
if(b.R&&0<b.timeout){var g=b.R;var h=V(function(){e||(e=!0,f.abort(),W(h),g.call(b.context||y,f))},b.timeout)}return f}
function df(a,b){b.zb&&(a=document.location.protocol+"//"+document.location.hostname+(document.location.port?":"+document.location.port:"")+a);var c=R("XSRF_FIELD_NAME",void 0),d=b.hb;d&&(d[c]&&delete d[c],a=Oe(a,d||{},!0));return a}
function ef(a,b){var c=R("XSRF_FIELD_NAME",void 0),d=R("XSRF_TOKEN",void 0),e=b.postBody||"",f=b.D,g=R("XSRF_FIELD_NAME",void 0),h;b.headers&&(h=b.headers["Content-Type"]);b.yb||K(a)&&!b.withCredentials&&K(a)!=document.location.hostname||"POST"!=b.method||h&&"application/x-www-form-urlencoded"!=h||b.D&&b.D[g]||(f||(f={}),f[c]=d);f&&"string"===typeof e&&(e=Ne(e),pb(e,f),e=b.wa&&"JSON"==b.wa?JSON.stringify(e):ac(e));f=e||f&&!jb(f);!$e&&f&&"POST"!=b.method&&($e=!0,S(Error("AJAX request with postData should use POST")));
return e}
function hf(a,b,c,d){var e=null;switch(b){case "JSON":try{var f=c.responseText}catch(g){throw d=Error("Error reading responseText"),d.params=a,Ke(d),g;}a=c.getResponseHeader("Content-Type")||"";f&&0<=a.indexOf("json")&&(e=JSON.parse(f));break;case "XML":if(a=(a=c.responseXML)?jf(a):null)e={},H(a.getElementsByTagName("*"),function(g){e[g.tagName]=kf(g)})}d&&lf(e);
return e}
function lf(a){if(Ma(a))for(var b in a){var c;(c="html_content"==b)||(c=b.length-5,c=0<=c&&b.indexOf("_html",c)==c);if(c){c=b;var d=Sb(a[b],null);a[c]=d}else lf(a[b])}}
function jf(a){return a?(a=("responseXML"in a?a.responseXML:a).getElementsByTagName("root"))&&0<a.length?a[0]:null:null}
function kf(a){var b="";H(a.childNodes,function(c){b+=c.nodeValue});
return b}
function gf(a,b,c,d,e,f,g){function h(){4==(k&&"readyState"in k?k.readyState:0)&&b&&Je(b)(k)}
c=void 0===c?"GET":c;d=void 0===d?"":d;var k=We();if(!k)return null;"onloadend"in k?k.addEventListener("loadend",h,!1):k.onreadystatechange=h;T("debug_forward_web_query_parameters")&&(a=bf(a));k.open(c,a,!0);f&&(k.responseType=f);g&&(k.withCredentials=!0);c="POST"==c&&(void 0===window.FormData||!(d instanceof FormData));if(e=af(a,e))for(var l in e)k.setRequestHeader(l,e[l]),"content-type"==l.toLowerCase()&&(c=!1);c&&k.setRequestHeader("Content-Type","application/x-www-form-urlencoded");k.send(d);
return k}
;var mf=rc||sc;function nf(a){var b=Nb;return b?0<=b.toLowerCase().indexOf(a):!1}
;var of={},pf=0;
function qf(a,b,c,d,e){e=void 0===e?"":e;if(a)if(c&&!nf("cobalt")){if(a){a instanceof I||(a="object"==typeof a&&a.M?a.L():String(a),Kb.test(a)?a=new I(Fb,a):(a=String(a),a=a.replace(/(%0A|%0D)/g,""),a=(b=a.match(Jb))&&Ib.test(b[1])?new I(Fb,a):null));b=Hb(a||Mb);if("about:invalid#zClosurez"===b||b.startsWith("data"))a="";else{if(b instanceof Qb)a=b;else{var f="object"==typeof b;a=null;f&&b.ja&&(a=b.ga());b=xb(f&&b.M?b.L():String(b));a=Sb(b,a)}a instanceof Qb&&a.constructor===Qb&&a.h===Rb?a=a.f:(Ja(a),
a="type_error:SafeHtml");a=encodeURIComponent(String(Md(a.toString())))}/^[\s\xa0]*$/.test(a)||(a=Hc("IFRAME",{src:'javascript:"<body><img src=\\""+'+a+'+"\\"></body>"',style:"display:none"}),(9==a.nodeType?a:a.ownerDocument||a.document).body.appendChild(a))}}else if(e)gf(a,b,"POST",e,d);else if(R("USE_NET_AJAX_FOR_PING_TRANSPORT",!1)||d)gf(a,b,"GET","",d);else{b:{try{var g=new Va({url:a});if(g.h&&g.g||g.i){var h=Zb(a.match(Yb)[5]||null),k;if(!(k=!h||!h.endsWith("/aclk"))){var l=a.search(cc);d:{for(c=
0;0<=(c=a.indexOf("ri",c))&&c<l;){var m=a.charCodeAt(c-1);if(38==m||63==m){var p=a.charCodeAt(c+2);if(!p||61==p||38==p||35==p){var r=c;break d}}c+=3}r=-1}if(0>r)var q=null;else{var A=a.indexOf("&",r);if(0>A||A>l)A=l;r+=3;q=decodeURIComponent(a.substr(r,A-r).replace(/\+/g," "))}k="1"!==q}f=!k;break b}}catch(D){}f=!1}f?rf(a)?(b&&b(),f=!0):f=!1:f=!1;f||sf(a,b)}}
function rf(a,b){try{if(window.navigator&&window.navigator.sendBeacon&&window.navigator.sendBeacon(a,void 0===b?"":b))return!0}catch(c){}return!1}
function sf(a,b){var c=new Image,d=""+pf++;of[d]=c;c.onload=c.onerror=function(){b&&of[d]&&b();delete of[d]};
c.src=a}
;var tf=window.yt&&window.yt.msgs_||window.ytcfg&&window.ytcfg.msgs||{};z("yt.msgs_",tf,void 0);function uf(a){Be(tf,arguments)}
;function vf(a,b,c,d){Ac.set(""+a,b,{ra:c,path:"/",domain:void 0===d?"youtube.com":d,secure:!1})}
;function wf(a){a&&(a.dataset?a.dataset[xf("loaded")]="true":a.setAttribute("data-loaded","true"))}
function yf(a,b){return a?a.dataset?a.dataset[xf(b)]:a.getAttribute("data-"+b):null}
var zf={};function xf(a){return zf[a]||(zf[a]=String(a).replace(/\-([a-z])/g,function(b,c){return c.toUpperCase()}))}
;var Af=y.ytPubsubPubsubInstance||new P,Bf=y.ytPubsubPubsubSubscribedKeys||{},Cf=y.ytPubsubPubsubTopicToKeys||{},Df=y.ytPubsubPubsubIsSynchronous||{};function Ef(a,b){var c=Ff();if(c){var d=c.subscribe(a,function(){var e=arguments;var f=function(){Bf[d]&&b.apply&&"function"==typeof b.apply&&b.apply(window,e)};
try{Df[a]?f():V(f,0)}catch(g){S(g)}},void 0);
Bf[d]=!0;Cf[a]||(Cf[a]=[]);Cf[a].push(d);return d}return 0}
function Gf(a){var b=Ff();b&&("number"===typeof a?a=[a]:"string"===typeof a&&(a=[parseInt(a,10)]),H(a,function(c){b.unsubscribeByKey(c);delete Bf[c]}))}
function Hf(a,b){var c=Ff();c&&c.publish.apply(c,arguments)}
function If(a){var b=Ff();if(b)if(b.clear(a),a)Jf(a);else for(var c in Cf)Jf(c)}
function Ff(){return y.ytPubsubPubsubInstance}
function Jf(a){Cf[a]&&(a=Cf[a],H(a,function(b){Bf[b]&&delete Bf[b]}),a.length=0)}
P.prototype.subscribe=P.prototype.subscribe;P.prototype.unsubscribeByKey=P.prototype.P;P.prototype.publish=P.prototype.O;P.prototype.clear=P.prototype.clear;z("ytPubsubPubsubInstance",Af,void 0);z("ytPubsubPubsubTopicToKeys",Cf,void 0);z("ytPubsubPubsubIsSynchronous",Df,void 0);z("ytPubsubPubsubSubscribedKeys",Bf,void 0);var Kf=/\.vflset|-vfl[a-zA-Z0-9_+=-]+/,Lf=/-[a-zA-Z]{2,3}_[a-zA-Z]{2,3}(?=(\/|$))/;function Mf(a,b,c){c=void 0===c?null:c;if(window.spf&&spf.script){c="";if(a){var d=a.indexOf("jsbin/"),e=a.lastIndexOf(".js"),f=d+6;-1<d&&-1<e&&e>f&&(c=a.substring(f,e),c=c.replace(Kf,""),c=c.replace(Lf,""),c=c.replace("debug-",""),c=c.replace("tracing-",""))}spf.script.load(a,c,b)}else Nf(a,b,c)}
function Nf(a,b,c){c=void 0===c?null:c;var d=Of(a),e=document.getElementById(d),f=e&&yf(e,"loaded"),g=e&&!f;f?b&&b():(b&&(f=Ef(d,b),b=""+Na(b),Pf[b]=f),g||(e=Qf(a,d,function(){yf(e,"loaded")||(wf(e),Hf(d),V(Sa(If,d),0))},c)))}
function Qf(a,b,c,d){d=void 0===d?null:d;var e=Ic(document,"SCRIPT");e.id=b;e.onload=function(){c&&setTimeout(c,0)};
e.onreadystatechange=function(){switch(e.readyState){case "loaded":case "complete":e.onload()}};
d&&e.setAttribute("nonce",d);Ub(e,Mc(a));a=document.getElementsByTagName("head")[0]||document.body;a.insertBefore(e,a.firstChild);return e}
function Rf(a){a=Of(a);var b=document.getElementById(a);b&&(If(a),b.parentNode.removeChild(b))}
function Sf(a,b){if(a&&b){var c=""+Na(b);(c=Pf[c])&&Gf(c)}}
function Of(a){var b=document.createElement("a");Tb(b,a);a=b.href.replace(/^[a-zA-Z]+:\/\//,"//");return"js-"+Xb(a)}
var Pf={};function Tf(){}
function Uf(a,b){return Vf(a,0,b)}
function Wf(a,b){return Vf(a,1,b)}
;function Xf(){}
v(Xf,Tf);function Vf(a,b,c){isNaN(c)&&(c=void 0);var d=B("yt.scheduler.instance.addJob");return d?d(a,b,c):void 0===c?(a(),NaN):V(a,c||0)}
function Yf(a){if(!isNaN(a)){var b=B("yt.scheduler.instance.cancelJob");b?b(a):W(a)}}
Xf.prototype.start=function(){var a=B("yt.scheduler.instance.start");a&&a()};
Xf.prototype.pause=function(){var a=B("yt.scheduler.instance.pause");a&&a()};
Ia(Xf);Xf.getInstance();var Zf=[],$f=!1;function ag(){if(!T("disable_ad_status_on_html5_clients")&&(!T("condition_ad_status_fetch_on_consent_cookie_html5_clients")||Ac.get("CONSENT","").startsWith("YES+"))&&"1"!=gb(De(),"args","privembed")){var a=function(){$f=!0;"google_ad_status"in window?Q("DCLKSTAT",1):Q("DCLKSTAT",2)};
Mf("//static.doubleclick.net/instream/ad_status.js",a);Zf.push(Wf(function(){$f||"google_ad_status"in window||(Sf("//static.doubleclick.net/instream/ad_status.js",a),$f=!0,Q("DCLKSTAT",3))},5E3))}}
function bg(){return parseInt(R("DCLKSTAT",0),10)}
;var cg=0;z("ytDomDomGetNextId",B("ytDomDomGetNextId")||function(){return++cg},void 0);var dg={stopImmediatePropagation:1,stopPropagation:1,preventMouseEvent:1,preventManipulation:1,preventDefault:1,layerX:1,layerY:1,screenX:1,screenY:1,scale:1,rotation:1,webkitMovementX:1,webkitMovementY:1};
function eg(a){this.type="";this.state=this.source=this.data=this.currentTarget=this.relatedTarget=this.target=null;this.charCode=this.keyCode=0;this.metaKey=this.shiftKey=this.ctrlKey=this.altKey=!1;this.clientY=this.clientX=0;this.changedTouches=this.touches=null;try{if(a=a||window.event){this.event=a;for(var b in a)b in dg||(this[b]=a[b]);var c=a.target||a.srcElement;c&&3==c.nodeType&&(c=c.parentNode);this.target=c;var d=a.relatedTarget;if(d)try{d=d.nodeName?d:null}catch(e){d=null}else"mouseover"==
this.type?d=a.fromElement:"mouseout"==this.type&&(d=a.toElement);this.relatedTarget=d;this.clientX=void 0!=a.clientX?a.clientX:a.pageX;this.clientY=void 0!=a.clientY?a.clientY:a.pageY;this.keyCode=a.keyCode?a.keyCode:a.which;this.charCode=a.charCode||("keypress"==this.type?this.keyCode:0);this.altKey=a.altKey;this.ctrlKey=a.ctrlKey;this.shiftKey=a.shiftKey;this.metaKey=a.metaKey;this.f=a.pageX;this.g=a.pageY}}catch(e){}}
function fg(a){if(document.body&&document.documentElement){var b=document.body.scrollTop+document.documentElement.scrollTop;a.f=a.clientX+(document.body.scrollLeft+document.documentElement.scrollLeft);a.g=a.clientY+b}}
eg.prototype.preventDefault=function(){this.event&&(this.event.returnValue=!1,this.event.preventDefault&&this.event.preventDefault())};
eg.prototype.stopPropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopPropagation&&this.event.stopPropagation())};
eg.prototype.stopImmediatePropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopImmediatePropagation&&this.event.stopImmediatePropagation())};var ib=y.ytEventsEventsListeners||{};z("ytEventsEventsListeners",ib,void 0);var gg=y.ytEventsEventsCounter||{count:0};z("ytEventsEventsCounter",gg,void 0);
function hg(a,b,c,d){d=void 0===d?{}:d;a.addEventListener&&("mouseenter"!=b||"onmouseenter"in document?"mouseleave"!=b||"onmouseenter"in document?"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"):b="mouseout":b="mouseover");return hb(function(e){var f="boolean"===typeof e[4]&&e[4]==!!d,g=Ma(e[4])&&Ma(d)&&lb(e[4],d);return!!e.length&&e[0]==a&&e[1]==b&&e[2]==c&&(f||g)})}
var ig=Xa(function(){var a=!1;try{var b=Object.defineProperty({},"capture",{get:function(){a=!0}});
window.addEventListener("test",null,b)}catch(c){}return a});
function jg(a,b,c,d){d=void 0===d?{}:d;if(!a||!a.addEventListener&&!a.attachEvent)return"";var e=hg(a,b,c,d);if(e)return e;e=++gg.count+"";var f=!("mouseenter"!=b&&"mouseleave"!=b||!a.addEventListener||"onmouseenter"in document);var g=f?function(h){h=new eg(h);if(!Lc(h.relatedTarget,function(k){return k==a}))return h.currentTarget=a,h.type=b,c.call(a,h)}:function(h){h=new eg(h);
h.currentTarget=a;return c.call(a,h)};
g=Je(g);a.addEventListener?("mouseenter"==b&&f?b="mouseover":"mouseleave"==b&&f?b="mouseout":"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"),ig()||"boolean"===typeof d?a.addEventListener(b,g,d):a.addEventListener(b,g,!!d.capture)):a.attachEvent("on"+b,g);ib[e]=[a,b,c,g,d];return e}
function kg(a){a&&("string"==typeof a&&(a=[a]),H(a,function(b){if(b in ib){var c=ib[b],d=c[0],e=c[1],f=c[3];c=c[4];d.removeEventListener?ig()||"boolean"===typeof c?d.removeEventListener(e,f,c):d.removeEventListener(e,f,!!c.capture):d.detachEvent&&d.detachEvent("on"+e,f);delete ib[b]}}))}
;var lg=window.ytcsi&&window.ytcsi.now?window.ytcsi.now:window.performance&&window.performance.timing&&window.performance.now&&window.performance.timing.navigationStart?function(){return window.performance.timing.navigationStart+window.performance.now()}:function(){return(new Date).getTime()};function mg(a){this.u=a;this.f=null;this.j=0;this.m=null;this.l=0;this.h=[];for(a=0;4>a;a++)this.h.push(0);this.i=0;this.F=jg(window,"mousemove",C(this.G,this));a=C(this.C,this);"function"===typeof a&&(a=Je(a));this.K=window.setInterval(a,25)}
F(mg,M);mg.prototype.G=function(a){void 0===a.f&&fg(a);var b=a.f;void 0===a.g&&fg(a);this.f=new Cc(b,a.g)};
mg.prototype.C=function(){if(this.f){var a=lg();if(0!=this.j){var b=this.m,c=this.f,d=b.x-c.x;b=b.y-c.y;d=Math.sqrt(d*d+b*b)/(a-this.j);this.h[this.i]=.5<Math.abs((d-this.l)/this.l)?1:0;for(c=b=0;4>c;c++)b+=this.h[c]||0;3<=b&&this.u();this.l=d}this.j=a;this.m=this.f;this.i=(this.i+1)%4}};
mg.prototype.o=function(){window.clearInterval(this.K);kg(this.F)};var ng={};
function og(a){var b=void 0===a?{}:a;a=void 0===b.Ja?!0:b.Ja;b=void 0===b.Va?!1:b.Va;if(null==B("_lact",window)){var c=parseInt(R("LACT"),10);c=isFinite(c)?E()-Math.max(c,0):-1;z("_lact",c,window);z("_fact",c,window);-1==c&&pg();jg(document,"keydown",pg);jg(document,"keyup",pg);jg(document,"mousedown",pg);jg(document,"mouseup",pg);a&&(b?jg(window,"touchmove",function(){qg("touchmove",200)},{passive:!0}):(jg(window,"resize",function(){qg("resize",200)}),jg(window,"scroll",function(){qg("scroll",200)})));
new mg(function(){qg("mouse",100)});
jg(document,"touchstart",pg,{passive:!0});jg(document,"touchend",pg,{passive:!0})}}
function qg(a,b){ng[a]||(ng[a]=!0,Wf(function(){pg();ng[a]=!1},b))}
function pg(){null==B("_lact",window)&&og();var a=E();z("_lact",a,window);-1==B("_fact",window)&&z("_fact",a,window);(a=B("ytglobal.ytUtilActivityCallback_"))&&a()}
function rg(){var a=B("_lact",window),b;null==a?b=-1:b=Math.max(E()-a,0);return b}
;var sg=window,X=sg.ytcsi&&sg.ytcsi.now?sg.ytcsi.now:sg.performance&&sg.performance.timing&&sg.performance.now&&sg.performance.timing.navigationStart?function(){return sg.performance.timing.navigationStart+sg.performance.now()}:function(){return(new Date).getTime()};var tg=Ue("initial_gel_batch_timeout",1E3),ug=Math.pow(2,16)-1,vg=null,wg=0,xg=void 0,yg=0,zg=0,Ag=0,Bg=!0,Cg=y.ytLoggingTransportLogPayloadsQueue_||{};z("ytLoggingTransportLogPayloadsQueue_",Cg,void 0);var Dg=y.ytLoggingTransportGELQueue_||new Map;z("ytLoggingTransportGELQueue_",Dg,void 0);var Eg=y.ytLoggingTransportTokensToCttTargetIds_||{};z("ytLoggingTransportTokensToCttTargetIds_",Eg,void 0);
function Fg(){W(yg);W(zg);zg=0;xg&&xg.isReady()?(Gg(Dg),"log_event"in Cg&&Gg(Object.entries(Cg.log_event)),Dg.clear(),delete Cg.log_event):Hg()}
function Hg(){T("web_gel_timeout_cap")&&!zg&&(zg=V(Fg,6E4));W(yg);var a=R("LOGGING_BATCH_TIMEOUT",Ue("web_gel_debounce_ms",1E4));T("shorten_initial_gel_batch_timeout")&&Bg&&(a=tg);yg=V(Fg,a)}
function Gg(a){var b=xg,c=Math.round(X());a=u(a);for(var d=a.next();!d.done;d=a.next()){var e=u(d.value);d=e.next().value;var f=e.next().value;e=nb({context:Ig(b.f||Jg())});e.events=f;(f=Eg[d])&&Kg(e,d,f);delete Eg[d];Lg(e,c);Mg(b,"log_event",e,{retry:!0,onSuccess:function(){wg=Math.round(X()-c)}});
Bg=!1}}
function Lg(a,b){a.requestTimeMs=String(b);T("unsplit_gel_payloads_in_logs")&&(a.unsplitGelPayloadsInLogs=!0);var c=R("EVENT_ID",void 0);if(c){var d=R("BATCH_CLIENT_COUNTER",void 0)||0;!d&&T("web_client_counter_random_seed")&&(d=Math.floor(Math.random()*ug/2));d++;d>ug&&(d=1);Q("BATCH_CLIENT_COUNTER",d);c={serializedEventId:c,clientCounter:String(d)};a.serializedClientEventId=c;vg&&wg&&T("log_gel_rtt_web")&&(a.previousBatchInfo={serializedClientEventId:vg,roundtripMs:String(wg)});vg=c;wg=0}}
function Kg(a,b,c){if(c.videoId)var d="VIDEO";else if(c.playlistId)d="PLAYLIST";else return;a.credentialTransferTokenTargetId=c;a.context=a.context||{};a.context.user=a.context.user||{};a.context.user.credentialTransferTokens=[{token:b,scope:d}]}
;var Ng=y.ytLoggingGelSequenceIdObj_||{};z("ytLoggingGelSequenceIdObj_",Ng,void 0);
function Og(a,b,c,d){d=void 0===d?{}:d;var e={};e.eventTimeMs=Math.round(d.timestamp||X());e[a]=b;e.context={lastActivityMs:String(d.timestamp?-1:rg())};T("log_sequence_info_on_gel_web")&&d.S&&(a=e.context,b=d.S,Ng[b]=b in Ng?Ng[b]+1:0,a.sequence={index:Ng[b],groupKey:b},d.xb&&delete Ng[d.S]);d=d.fa;a="";d&&(a={},d.videoId?a.videoId=d.videoId:d.playlistId&&(a.playlistId=d.playlistId),Eg[d.token]=a,a=d.token);d=Dg.get(a)||[];Dg.set(a,d);d.push(e);c&&(xg=new c);c=Ue("web_logging_max_batch")||100;e=
X();d.length>=c?Fg():10<=e-Ag&&(Hg(),Ag=e)}
;function Pg(){for(var a={},b=u(Object.entries(Ne(R("DEVICE","")))),c=b.next();!c.done;c=b.next()){var d=u(c.value);c=d.next().value;d=d.next().value;"cbrand"===c?a.deviceMake=d:"cmodel"===c?a.deviceModel=d:"cbr"===c?a.browserName=d:"cbrver"===c?a.browserVersion=d:"cos"===c?a.osName=d:"cosver"===c?a.osVersion=d:"cplatform"===c&&(a.platform=d)}return a}
;function Qg(){return"INNERTUBE_API_KEY"in Ce&&"INNERTUBE_API_VERSION"in Ce}
function Jg(){return{innertubeApiKey:R("INNERTUBE_API_KEY",void 0),innertubeApiVersion:R("INNERTUBE_API_VERSION",void 0),Ka:R("INNERTUBE_CONTEXT_CLIENT_CONFIG_INFO"),La:R("INNERTUBE_CONTEXT_CLIENT_NAME","WEB"),innertubeContextClientVersion:R("INNERTUBE_CONTEXT_CLIENT_VERSION",void 0),Na:R("INNERTUBE_CONTEXT_HL",void 0),Ma:R("INNERTUBE_CONTEXT_GL",void 0),Oa:R("INNERTUBE_HOST_OVERRIDE",void 0)||"",Qa:!!R("INNERTUBE_USE_THIRD_PARTY_AUTH",!1),Pa:!!R("INNERTUBE_OMIT_API_KEY_WHEN_AUTH_HEADER_IS_PRESENT",
!1)}}
function Ig(a){a={client:{hl:a.Na,gl:a.Ma,clientName:a.La,clientVersion:a.innertubeContextClientVersion,configInfo:a.Ka}};var b=window.devicePixelRatio;b&&1!=b&&(a.client.screenDensityFloat=String(b));b=R("EXPERIMENTS_TOKEN","");""!==b&&(a.client.experimentsToken=b);b=[];var c=R("EXPERIMENTS_FORCED_FLAGS",{});for(d in c)b.push({key:d,value:String(c[d])});var d=R("EXPERIMENT_FLAGS",{});for(var e in d)e.startsWith("force_")&&void 0===c[e]&&b.push({key:e,value:String(d[e])});0<b.length&&(a.request={internalExperimentFlags:b});
R("DELEGATED_SESSION_ID")&&!T("pageid_as_header_web")&&(a.user={onBehalfOfUser:R("DELEGATED_SESSION_ID")});a.client=Object.assign(a.client,Pg());return a}
function Rg(a,b,c){c=void 0===c?{}:c;var d={"X-Goog-Visitor-Id":c.visitorData||R("VISITOR_DATA","")};if(b&&b.includes("www.youtube-nocookie.com"))return d;(b=c.ub||R("AUTHORIZATION"))||(a?b="Bearer "+B("gapi.auth.getToken")().tb:b=ed([]));b&&(d.Authorization=b,d["X-Goog-AuthUser"]=R("SESSION_INDEX",0),T("pageid_as_header_web")&&(d["X-Goog-PageId"]=R("DELEGATED_SESSION_ID")));return d}
;function Sg(a){a=Object.assign({},a);delete a.Authorization;var b=ed();if(b){var c=new xd;c.update(R("INNERTUBE_API_KEY",void 0));c.update(b);b=c.digest();c=3;Ka(b);void 0===c&&(c=0);if(!uc){uc={};for(var d="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".split(""),e=["+/=","+/","-_=","-_.","-_"],f=0;5>f;f++){var g=d.concat(e[f].split(""));tc[f]=g;for(var h=0;h<g.length;h++){var k=g[h];void 0===uc[k]&&(uc[k]=h)}}}c=tc[c];d=[];for(e=0;e<b.length;e+=3){var l=b[e],m=(f=e+1<b.length)?
b[e+1]:0;k=(g=e+2<b.length)?b[e+2]:0;h=l>>2;l=(l&3)<<4|m>>4;m=(m&15)<<2|k>>6;k&=63;g||(k=64,f||(m=64));d.push(c[h],c[l],c[m]||"",c[k]||"")}a.hash=d.join("")}return a}
function Tg(a){a=Sg(a);var b=new xd;b.update(JSON.stringify(a,Object.keys(a).sort()));a=b.digest();b="";for(var c=0;c<a.length;c++)b+="0123456789ABCDEF".charAt(Math.floor(a[c]/16))+"0123456789ABCDEF".charAt(a[c]%16);return b}
;function Ug(){var a=new ue;(a=a.isAvailable()?new Ae(a,"yt.innertube"):null)||(a=new ve("yt.innertube"),a=a.isAvailable()?a:null);this.f=a?new qe(a):null;this.g=document.domain||window.location.hostname}
Ug.prototype.set=function(a,b,c,d){c=c||31104E3;this.remove(a);if(this.f)try{this.f.set(a,b,E()+1E3*c);return}catch(f){}var e="";if(d)try{e=escape(Md(b))}catch(f){return}else e=escape(b);vf(a,e,c,this.g)};
Ug.prototype.get=function(a,b){var c=void 0,d=!this.f;if(!d)try{c=this.f.get(a)}catch(e){d=!0}if(d&&(c=Ac.get(""+a,void 0))&&(c=unescape(c),b))try{c=JSON.parse(c)}catch(e){this.remove(a),c=void 0}return c};
Ug.prototype.remove=function(a){this.f&&this.f.remove(a);var b=this.g;Ac.remove(""+a,"/",void 0===b?"youtube.com":b)};var Vg;function Wg(){Vg||(Vg=new Ug);return Vg}
function Xg(a,b,c,d){if(d)return null;d=Wg().get("nextId",!0)||1;var e=Wg().get("requests",!0)||{};e[d]={method:a,request:b,authState:Sg(c),requestTime:Math.round(X())};Wg().set("nextId",d+1,86400,!0);Wg().set("requests",e,86400,!0);return d}
function Yg(a){var b=Wg().get("requests",!0)||{};delete b[a];Wg().set("requests",b,86400,!0)}
function Zg(a){var b=Wg().get("requests",!0);if(b){for(var c in b){var d=b[c];if(!(6E4>Math.round(X())-d.requestTime)){var e=d.authState,f=Sg(Rg(!1));lb(e,f)&&(e=d.request,"requestTimeMs"in e&&(e.requestTimeMs=Math.round(X())),Mg(a,d.method,e,{}));delete b[c]}}Wg().set("requests",b,86400,!0)}}
;function $g(){}
;function ah(a){if(!a)throw Error();throw a;}
function bh(a){return a}
function ch(a){var b=this;this.g=a;this.state={status:"PENDING"};this.f=[];this.onRejected=[];this.g(function(c){if("PENDING"===b.state.status){b.state={status:"FULFILLED",value:c};c=u(b.f);for(var d=c.next();!d.done;d=c.next())d=d.value,d()}},function(c){if("PENDING"===b.state.status){b.state={status:"REJECTED",
reason:c};c=u(b.onRejected);for(var d=c.next();!d.done;d=c.next())d=d.value,d()}})}
function dh(){return new ch(function(a){a(void 0)})}
ch.prototype.then=function(a,b){var c=this,d=null!==a&&void 0!==a?a:bh,e=null!==b&&void 0!==b?b:ah;return new ch(function(f,g){"PENDING"===c.state.status?(c.f.push(function(){eh(c,c,d,f,g)}),c.onRejected.push(function(){fh(c,c,e,f,g)})):"FULFILLED"===c.state.status?eh(c,c,d,f,g):"REJECTED"===c.state.status&&fh(c,c,e,f,g)})};
function gh(a,b){a.then(void 0,b)}
function eh(a,b,c,d,e){try{if("FULFILLED"!==a.state.status)throw Error("calling handleResolve before the promise is fulfilled.");var f=c(a.state.value);f instanceof ch?hh(a,b,f,d,e):d(f)}catch(g){e(g)}}
function fh(a,b,c,d,e){try{if("REJECTED"!==a.state.status)throw Error("calling handleReject before the promise is rejected.");var f=c(a.state.reason);f instanceof ch?hh(a,b,f,d,e):d(f)}catch(g){e(g)}}
function hh(a,b,c,d,e){b===c?e(new TypeError("Circular promise chain detected.")):c.then(function(f){f instanceof ch?hh(a,b,f,d,e):d(f)},function(f){e(f)})}
;function ih(){var a=Error.call(this,"Transaction was aborted");this.message=a.message;"stack"in a&&(this.stack=a.stack);Object.setPrototypeOf(this,ih.prototype)}
v(ih,Error);function jh(a){return a instanceof DOMException?"VersionError"===a.name:"DOMError"in self&&a instanceof DOMError?"VersionError"===a.name:a instanceof Object&&"message"in a?"An attempt was made to open a database using a lower version than the existing version."===a.message:!1}
function kh(a,b){return new ch(function(c,d){function e(){var f=a?b(a):null;f?f.then(function(g){a=g;e()},d):c()}
e()})}
;function lh(a){return new O(function(b,c){function d(){c(a.error);f()}
function e(){b(a.result);f()}
function f(){a.removeEventListener("success",e);a.removeEventListener("error",d)}
a.addEventListener("success",e);a.addEventListener("error",d)})}
function mh(a){return new ch(function(b,c){function d(){c(a.error);f()}
function e(){b(a.result);f()}
function f(){a.removeEventListener("success",e);a.removeEventListener("error",d)}
a.addEventListener("success",e);a.addEventListener("error",d)})}
;function nh(a){this.f=a}
n=nh.prototype;n.add=function(a,b,c){return oh(this,[a],"readwrite",function(d){return ph(d,a).add(b,c)})};
n.clear=function(a){return oh(this,[a],"readwrite",function(b){return ph(b,a).clear()})};
n.close=function(){this.f.close()};
n.count=function(a,b){return oh(this,[a],"readonly",function(c){return ph(c,a).count(b)})};
function qh(a,b,c){a=a.f.createObjectStore(b,c);return new rh(a)}
n["delete"]=function(a,b){return oh(this,[a],"readwrite",function(c){return ph(c,a)["delete"](b)})};
n.get=function(a,b){return oh(this,[a],"readwrite",function(c){return ph(c,a).get(b)})};
function sh(a,b){return oh(a,["databases"],"readwrite",function(c){return th(ph(c,"databases"),b,void 0)})}
function oh(a,b,c,d){c=void 0===c?"readonly":c;return new O(function(e,f){var g=a.f.transaction(b,c),h=new uh(g,b);gh(d(h).then(function(k){$d(vh(h).then(function(){e(k)}),function(l){f(l)})}),function(k){f(k)})})}
function rh(a){this.f=a}
n=rh.prototype;n.add=function(a,b){var c=b?this.f.add(a,b):this.f.add(a);return mh(c)};
n.clear=function(){return mh(this.f.clear()).then(function(){})};
n.count=function(a){a=a?this.f.count(a):this.f.count();return mh(a)};
n["delete"]=function(a){return mh(this.f["delete"](a))};
n.get=function(a){return mh(this.f.get(a))};
n.index=function(a){return new wh(this.f.index(a))};
n.getName=function(){return this.f.name};
function th(a,b,c){a=c?a.f.put(b,c):a.f.put(b);return mh(a)}
function uh(a){var b=this;this.f=a;this.g=new Map;this.aborted=!1;this.done=new O(function(c,d){b.f.addEventListener("complete",function(){c()});
b.f.addEventListener("error",function(e){e.currentTarget===e.target&&d(b.f.error)});
b.f.addEventListener("abort",function(){var e=b.f.error;e?("QuotaExceededError"===e.name?Ke(Error("The current transaction exceeded its quota limitations.")):"UnknownError"===e.name&&Ke(Error("The current transaction may have failed because of exceeding quota limitations.")),d(e)):d(new ih)})})}
uh.prototype.abort=function(){this.f.abort();this.aborted=!0};
function vh(a){var b=a.f;b.commit&&!a.aborted&&b.commit();return a.done}
function ph(a,b){var c=a.f.objectStore(b),d=a.g.get(c);d||(d=new rh(c),a.g.set(c,d));return d}
function wh(a){this.f=a}
wh.prototype.count=function(a){a=a?this.f.count(a):this.f.count();return mh(a)};
wh.prototype.get=function(a){return mh(this.f.get(a))};
function xh(a,b,c){var d=b.query;b=b.direction;a=d&&b?a.f.openCursor(d,b):d?a.f.openCursor(d):a.f.openCursor();return yh(a).then(function(e){return kh(e,c)})}
function zh(a,b){this.request=a;this.f=b}
function yh(a){return mh(a).then(function(b){return null===b?null:new zh(a,b)})}
zh.prototype["delete"]=function(){return mh(this.f["delete"]()).then(function(){})};
zh.prototype.getValue=function(){return this.f.value};
zh.prototype.update=function(a){return mh(this.f.update(a))};function Ah(a,b,c){function d(){m||(m=new nh(f.result));return m}
var e=uh;var f=void 0!==b?self.indexedDB.open(a,b):self.indexedDB.open(a);var g=c.blocked,h=c.blocking,k=c.f,l=c.upgrade,m;l&&f.addEventListener("upgradeneeded",function(p){if(null===p.newVersion)throw Error("Invariant: newVersion on IDbVersionChangeEvent is null");if(null===f.transaction)throw Error("Invariant: transaction on IDbOpenDbRequest is null");var r=d(),q=new e(f.transaction);l(r,p.oldVersion,p.newVersion,q)});
g&&f.addEventListener("blocked",function(){g()});
return lh(f).then(function(p){h&&p.addEventListener("versionchange",function(){h(d())});
k&&p.addEventListener("close",function(){k()});
return d()})}
function Bh(a,b,c){c=void 0===c?{}:c;return Ah(a,b,c)}
;var Ch,Dh,Eh=["getAll","getAllKeys","getKey","openKeyCursor"],Fh=["getAll","getAllKeys","getKey","openKeyCursor"];function Gh(){var a;if(a=mf)a=/WebKit\/([0-9]+)/.exec(Nb),a=!!(a&&600<=parseInt(a[1],10));a&&(a=/WebKit\/([0-9]+)/.exec(Nb),a=!(a&&602<=parseInt(a[1],10)));return a&&!T("ytidb_allow_on_ios_safari_v8_and_v9")?!1:!!self.indexedDB}
function Hh(){return new Promise(function(a){setTimeout(a,50)})}
function Ih(){return N(this,function b(){var c,d,e;return x(b,function(f){switch(f.f){case 1:if(!Gh())return f["return"](!1);ra(f);d=!1;return w(f,Bh("yt-idb-test-do-not-use",void 0,{blocking:function(){d=!0;c&&(c.close(),c=void 0)}}),5);
case 5:return c=f.g,e=Bh("yt-idb-test-do-not-use",c.f.version+1).then(function(g){try{g.close()}catch(h){}}),w(f,Promise.race([e,
Hh()]),6);case 6:return f["return"](d);case 3:ta(f);if(c)try{c.close()}catch(g){}ua(f);break;case 2:return sa(f),f["return"](!1)}})})}
function Jh(){return void 0!==Ch?Xd(Ch):new O(function(a){Ih().then(function(b){Ch=b;a(b)})})}
function Kh(){return void 0!==Dh?Xd(Dh):Jh().then(function(a){if(!a)return!1;var b=u(Eh);for(a=b.next();!a.done;a=b.next())if(!IDBObjectStore.prototype[a.value])return!1;b=u(Fh);for(a=b.next();!a.done;a=b.next())if(!IDBIndex.prototype[a.value])return!1;return IDBObjectStore.prototype.getKey?!0:!1}).then(function(a){return Dh=a})}
;var Lh;function Mh(){function a(b){b.close();Lh=void 0}
Lh||(Lh=$d(Bh("YtIdbMeta",1,{blocking:a,upgrade:function(b,c){1>c&&qh(b,"databases",{keyPath:"actualName"})}}),function(b){return jh(b)?Bh("YtIdbMeta",void 0,{blocking:a}):Yd(b)}));
return Lh}
function Nh(a){return Mh().then(function(b){return b.get("databases",a.actualName).then(function(c){if(c?a.actualName!==c.actualName||a.publicName!==c.publicName||a.userIdentifier!==c.userIdentifier||a.signedIn!==c.signedIn:1)return sh(b,a)})})}
function Oh(a){return Mh().then(function(b){return b["delete"]("databases",a)})}
;function Ph(a){try{var b={actualName:"LogsDataBase",publicName:"LogsDataBase",userIdentifier:void 0,signedIn:!1}}catch(c){return Yd(c)}return $d(Nh(b).then(function(){return a(b)}),function(c){return $d(Oh(b.actualName),function(){}).then(function(){return Yd(c)})})}
function Qh(a,b){b=void 0===b?{}:b;return Ph(function(c){return Bh(c.actualName,a,b)})}
;var Rh;function Sh(){return N(this,function b(){return x(b,function(c){if(!Rh)try{Rh=Qh(1,{upgrade:function(d,e){1>e&&(qh(d,"LogsRequestsStore",{keyPath:"id",autoIncrement:!0}).f.createIndex("newRequest",["status","authHash","timestamp"],{unique:!1}),qh(d,"sapisid"))}})}catch(d){if(!jh(d))return S(d),c["return"](Promise.reject(d));
Rh=Qh()}return c["return"](Rh)})})}
function Th(a){return N(this,function c(){var d,e,f;return x(c,function(g){if(1==g.f)return w(g,Uh(),2);if(3!=g.f)return d=g.g,w(g,Sh(),3);e=g.g;f=Object.assign(Object.assign({},a),{options:JSON.parse(JSON.stringify(a.options)),authHash:d});return g["return"](e.add("LogsRequestsStore",f))})})}
function Vh(){return N(this,function b(){var c,d,e,f,g,h;return x(b,function(k){switch(k.f){case 1:return w(k,Uh(),2);case 2:return c=k.g,d=["NEW",c,0],e=["NEW",c,X()],f=IDBKeyRange.bound(d,e),w(k,Sh(),3);case 3:return g=k.g,h=void 0,w(k,oh(g,["LogsRequestsStore"],"readwrite",function(l){return xh(ph(l,"LogsRequestsStore").index("newRequest"),{query:f,direction:"prev"},function(m){m.getValue()&&(h=m.getValue(),h.status="QUEUED",m.update(h))})}),4);
case 4:return k["return"](h)}})})}
function Wh(a){return N(this,function c(){var d;return x(c,function(e){if(1==e.f)return w(e,Sh(),2);d=e.g;return e["return"](oh(d,["LogsRequestsStore"],"readwrite",function(f){var g=ph(f,"LogsRequestsStore");return g.get(a).then(function(h){if(h)return h.status="QUEUED",th(g,h).then(function(){return h})})}))})})}
function Xh(a){return N(this,function c(){var d;return x(c,function(e){if(1==e.f)return w(e,Sh(),2);d=e.g;return e["return"](oh(d,["LogsRequestsStore"],"readwrite",function(f){var g=ph(f,"LogsRequestsStore");return g.get(a).then(function(h){return h?(h.status="NEW",h.sendCount+=1,th(g,h).then(function(){return h})):dh()})}))})})}
function Yh(){return N(this,function b(){var c,d;return x(b,function(e){if(1==e.f)return w(e,Sh(),2);if(3!=e.f)return c=e.g,w(e,c.count("LogsRequestsStore"),3);d=e.g;return e["return"](!d)})})}
function Zh(a){return N(this,function c(){var d;return x(c,function(e){if(1==e.f)return w(e,Sh(),2);d=e.g;return e["return"](d["delete"]("LogsRequestsStore",a))})})}
function Uh(){return N(this,function b(){var c;return x(b,function(d){if(1==d.f){$g.f||($g.f=new $g);var e={};var f=ed([]);f&&(e.Authorization=f,e["X-Goog-AuthUser"]=R("SESSION_INDEX",0),"INNERTUBE_HOST_OVERRIDE"in Ce||(e["X-Origin"]=window.location.origin),T("pageid_as_header_web")&&"DELEGATED_SESSION_ID"in Ce&&(e["X-Goog-PageId"]=R("DELEGATED_SESSION_ID")));e=Xd(e);return w(d,e,2)}c=d.g;return d["return"](Tg(c))})})}
;var $h=Ue("network_polling_interval",3E4);function ai(){this.i=0;this.f=window.navigator.onLine;bi(this);ci(this)}
function di(){ai.f||(ai.f=new ai);return ai.f}
function ei(a){var b=fi,c=gi;(new O(function(d){a.g=d})).then(function(){b();
c&&(a.h=c)});
hi(a)}
function ci(a){window.addEventListener("online",function(){a.f=!0;a.g&&a.g()})}
function bi(a){window.addEventListener("offline",function(){a.f=!1;a.h&&a.h()})}
function hi(a){a.i||(ii(a),window.navigator.onLine&&a.g&&a.g())}
function ii(a){a.i=Uf(function(){window.navigator.onLine?(!1===a.f&&S(Error("NetworkStatusManager missed online event.")),a.f=!0,a.g&&a.g()):(!0===a.f&&S(Error("NetworkStatusManager missed offline event.")),a.f=!1,a.h&&a.h());ii(a)},$h)}
;var ji=Ue("networkless_throttle_timeout")||100,ki=Ue("networkless_retry_attempts")||1,li=0;function mi(a,b){b=void 0===b?{}:b;ni().then(function(c){if(c&&!T("networkless_bypass_write")){var d={url:a,options:b,timestamp:X(),status:"NEW",sendCount:0};Th(d).then(function(e){d.id=e;e=di();e.f&&!T("networkless_always_offline")?oi(d):ei(e)})["catch"](function(e){oi(d);
S(e)})}else ff(a,b)})}
function fi(){li||(li=Wf(function(){oi();li=0;fi()},ji))}
function gi(){Yf(li);li=0}
function oi(a){N(this,function c(){var d=this,e,f,g,h;return x(c,function(k){switch(k.f){case 1:e=d;if(!a)return w(k,Vh(),6);if(!a.id){k.H(3);break}return w(k,Wh(a.id),5);case 5:a=k.g;if(!a)throw Error("The request cannot be found in the database.");k.H(3);break;case 6:if(a=k.g){k.H(3);break}return w(k,Yh(),8);case 8:return(f=k.g)&&gi(),k["return"]();case 3:if(pi(a))g=a.options.onError?a.options.onError:function(){},h=a.options.onSuccess?a.options.onSuccess:function(){},a.options.onError=function(l,
m){return N(e,function r(){return x(r,function(q){if(1==q.f)return a&&a.id?a.sendCount<ki?w(q,Xh(a.id),6):w(q,Zh(a.id),2):q.H(2);
2!=q.f&&(li||ei(di()),g(l,m));g(l,m);q.f=0})})},a.options.onSuccess=function(l,m){return N(e,function r(){return x(r,function(q){if(1==q.f)return a&&a.id?w(q,Zh(a.id),2):q.H(2);
h(l,m);q.f=0})})},ff(a.url,a.options);
else if(Ke(Error("Networkless Logging: Stored logs request expired age limit")),a.id)return w(k,Zh(a.id),0);k.H(0)}})})}
function pi(a){a=a.timestamp;return 2592E6<=X()-a?!1:!0}
function ni(){return T("networkless_logging")?2===Ue("networkless_ytidb_version")?Kh():Xd(Gh()):Xd(!1)}
;function qi(a,b){for(var c=[],d=1;d<arguments.length;++d)c[d-1]=arguments[d];d=Error.call(this,a);this.message=d.message;"stack"in d&&(this.stack=d.stack);this.args=[].concat(c instanceof Array?c:fa(u(c)))}
v(qi,Error);function ri(a){var b=this;this.f=null;a?this.f=a:Qg()&&(this.f=Jg());Uf(function(){Zg(b)},5E3)}
ri.prototype.isReady=function(){!this.f&&Qg()&&(this.f=Jg());return!!this.f};
function Mg(a,b,c,d){!R("VISITOR_DATA")&&"visitor_id"!==b&&.01>Math.random()&&Ke(new qi("Missing VISITOR_DATA when sending innertube request.",b,c,d));if(!a.isReady()){var e=new qi("innertube xhrclient not ready",b,c,d);S(e);e.sampleWeight=0;throw e;}var f={headers:{"Content-Type":"application/json"},method:"POST",D:c,wa:"JSON",R:function(){d.R()},
va:d.R,onSuccess:function(p,r){if(d.onSuccess)d.onSuccess(r)},
ua:function(p){if(d.onSuccess)d.onSuccess(p)},
onError:function(p,r){if(d.onError)d.onError(r)},
Ab:function(p){if(d.onError)d.onError(p)},
timeout:d.timeout,withCredentials:!0},g="";(e=a.f.Oa)&&(g=e);var h=a.f.Qa||!1,k=Rg(h,g,d);Object.assign(f.headers,k);f.headers.Authorization&&!g&&(f.headers["x-origin"]=window.location.origin);e="/youtubei/"+a.f.innertubeApiVersion+"/"+b;var l={alt:"json"};a.f.Pa&&f.headers.Authorization||(l.key=a.f.innertubeApiKey);var m=Oe(""+g+e,l||{},!0);ni().then(function(p){if(d.retry&&T("retry_web_logging_batches")&&"www.youtube-nocookie.com"!=g){if(T("networkless_gel")&&!p||!T("networkless_gel"))var r=Xg(b,
c,k,h);if(r){var q=f.onSuccess,A=f.ua;f.onSuccess=function(D,U){Yg(r);q(D,U)};
c.ua=function(D,U){Yg(r);A(D,U)}}}try{T("use_fetch_for_op_xhr")?cf(m,f):T("networkless_gel")&&d.retry?(f.method="POST",mi(m,f)):(f.method="POST",f.D||(f.D={}),ff(m,f))}catch(D){if("InvalidAccessError"==D.name)r&&(Yg(r),r=0),Ke(Error("An extension is blocking network request."));
else throw D;}r&&Uf(function(){Zg(a)},5E3)})}
;function si(a,b,c){c=void 0===c?{}:c;var d=ri;R("ytLoggingEventsDefaultDisabled",!1)&&ri==ri&&(d=null);Og(a,b,d,c)}
;var ti=[{sa:function(a){return"Cannot read property '"+a.key+"'"},
ma:{TypeError:[{regexp:/Cannot read property '([^']+)' of (null|undefined)/,groups:["key","value"]},{regexp:/\u65e0\u6cd5\u83b7\u53d6\u672a\u5b9a\u4e49\u6216 (null|undefined) \u5f15\u7528\u7684\u5c5e\u6027\u201c([^\u201d]+)\u201d/,groups:["value","key"]},{regexp:/\uc815\uc758\ub418\uc9c0 \uc54a\uc74c \ub610\ub294 (null|undefined) \ucc38\uc870\uc778 '([^']+)' \uc18d\uc131\uc744 \uac00\uc838\uc62c \uc218 \uc5c6\uc2b5\ub2c8\ub2e4./,groups:["value","key"]},{regexp:/No se puede obtener la propiedad '([^']+)' de referencia nula o sin definir/,
groups:["key"]},{regexp:/Unable to get property '([^']+)' of (undefined or null) reference/,groups:["key","value"]}],Error:[{regexp:/(Permission denied) to access property "([^']+)"/,groups:["reason","key"]}]}},{sa:function(a){return"Cannot call '"+a.key+"'"},
ma:{TypeError:[{regexp:/(?:([^ ]+)?\.)?([^ ]+) is not a function/,groups:["base","key"]},{regexp:/Object (.*) has no method '([^ ]+)'/,groups:["base","key"]},{regexp:/Object doesn't support property or method '([^ ]+)'/,groups:["key"]},{regexp:/\u30aa\u30d6\u30b8\u30a7\u30af\u30c8\u306f '([^']+)' \u30d7\u30ed\u30d1\u30c6\u30a3\u307e\u305f\u306f\u30e1\u30bd\u30c3\u30c9\u3092\u30b5\u30dd\u30fc\u30c8\u3057\u3066\u3044\u307e\u305b\u3093/,groups:["key"]},{regexp:/\uac1c\uccb4\uac00 '([^']+)' \uc18d\uc131\uc774\ub098 \uba54\uc11c\ub4dc\ub97c \uc9c0\uc6d0\ud558\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4./,
groups:["key"]}]}}];function ui(){this.f=[];this.g=[]}
var vi;var wi=new Set,xi=0,yi=["PhantomJS","Googlebot","TO STOP THIS SECURITY SCAN go/scan"];function zi(a){Ai(a,"WARNING")}
function Ai(a,b,c,d,e,f){f=void 0===f?{}:f;f.name=c||R("INNERTUBE_CONTEXT_CLIENT_NAME",1);f.version=d||R("INNERTUBE_CONTEXT_CLIENT_VERSION",void 0);c=f||{};b=void 0===b?"ERROR":b;b=void 0===b?"ERROR":b;var g=void 0===g?!1:g;if(a&&(T("console_log_js_exceptions")&&(d=[],d.push("Name: "+a.name),d.push("Message: "+a.message),a.hasOwnProperty("params")&&d.push("Error Params: "+JSON.stringify(a.params)),d.push("File name: "+a.fileName),d.push("Stacktrace: "+a.stack),window.console.log(d.join("\n"),a)),
(window&&window.yterr||g)&&!(5<=xi)&&0!==a.sampleWeight)){var h=vc(a);g=h.message||"Unknown Error";d=h.name||"UnknownError";e=h.lineNumber||"Not available";f=h.fileName||"Not available";h=h.stack||a.f||"Not available";if(a.hasOwnProperty("args")&&a.args&&a.args.length)for(var k=0,l=0;l<a.args.length;l++){var m=a.args[l],p="params."+l;k+=p.length;if(m)if(Array.isArray(m))for(var r=c,q=0;q<m.length&&!(m[q]&&(k+=Bi(q,m[q],p,r),500<k));q++);else if("object"===typeof m)for(r in r=void 0,q=c,m){if(m[r]&&
(k+=Bi(r,m[r],p,q),500<k))break}else c[p]=String(JSON.stringify(m)).substring(0,500),k+=c[p].length;else c[p]=String(JSON.stringify(m)).substring(0,500),k+=c[p].length;if(500<=k)break}else if(a.hasOwnProperty("params")&&a.params)if(m=a.params,"object"===typeof a.params)for(l in p=0,m){if(m[l]&&(k="params."+l,r=String(JSON.stringify(m[l])).substr(0,500),c[k]=r,p+=k.length+r.length,500<p))break}else c.params=String(JSON.stringify(m)).substr(0,500);navigator.vendor&&!c.hasOwnProperty("vendor")&&(c.vendor=
navigator.vendor);c={message:g,name:d,lineNumber:e,fileName:f,stack:h,params:c};a=Number(a.columnNumber);isNaN(a)||(c.lineNumber=c.lineNumber+":"+a);a=u(ti);for(g=a.next();!g.done;g=a.next())if(g=g.value,g.ma[c.name])for(e=u(g.ma[c.name]),d=e.next();!d.done;d=e.next())if(f=d.value,d=c.message.match(f.regexp)){c.params["error.original"]=d[0];e=f.groups;f={};for(h=0;h<e.length;h++)f[e[h]]=d[h+1],c.params["error."+e[h]]=d[h+1];c.message=g.sa(f);break}window.yterr&&"function"===typeof window.yterr&&window.yterr(c);
if(!(wi.has(c.message)||0<=c.stack.indexOf("/YouTubeCenter.js")||0<=c.stack.indexOf("/mytube.js"))){if(T("kevlar_gel_error_routing")){a=b;a:{g=u(yi);for(d=g.next();!d.done;d=g.next())if(nf(d.value.toLowerCase())){g=!0;break a}g=!1}if(!g){g={stackTrace:c.stack};c.fileName&&(g.filename=c.fileName);d=c.lineNumber&&c.lineNumber.split?c.lineNumber.split(":"):[];0!==d.length&&(1!==d.length||isNaN(Number(d[0]))?2!==d.length||isNaN(Number(d[0]))||isNaN(Number(d[1]))||(g.lineNumber=Number(d[0]),g.columnNumber=
Number(d[1])):g.lineNumber=Number(d[0]));d=c.message;e=c.name;vi||(vi=new ui);f=vi;a:{h=u(f.g);for(l=h.next();!l.done;l=h.next())if(l=l.value,c.message&&c.message.match(l.f)){f=l.weight;break a}f=u(f.f);for(h=f.next();!h.done;h=f.next())if(h=h.value,h.Ca(c)){f=h.weight;break a}f=1}d={level:"ERROR_LEVEL_UNKNOWN",message:d,errorClassName:e,sampleWeight:f};"ERROR"===a?d.level="ERROR_LEVEL_ERROR":"WARNING"===a&&(d.level="ERROR_LEVEL_WARNNING");a={isObfuscated:!0,browserStackInfo:g};g={pageUrl:window.location.href,
kvPairs:[]};if(e=c.params)for(f=u(Object.keys(e)),h=f.next();!h.done;h=f.next())h=h.value,g.kvPairs.push({key:"client."+h,value:String(e[h])});e=R("SERVER_NAME",void 0);f=R("SERVER_VERSION",void 0);e&&f&&(g.kvPairs.push({key:"server.name",value:e}),g.kvPairs.push({key:"server.version",value:f}));si("clientError",{errorMetadata:g,stackTrace:a,logMessage:d});Fg()}}a=c.params||{};b={hb:{a:"logerror",t:"jserror",type:c.name,msg:c.message.substr(0,250),line:c.lineNumber,level:b,"client.name":a.name},D:{url:R("PAGE_NAME",
window.location.href),file:c.fileName},method:"POST"};a.version&&(b["client.version"]=a.version);if(b.D){c.stack&&(b.D.stack=c.stack);g=u(Object.keys(a));for(d=g.next();!d.done;d=g.next())d=d.value,b.D["client."+d]=a[d];if(a=R("LATEST_ECATCHER_SERVICE_TRACKING_PARAMS",void 0))for(g=u(Object.keys(a)),d=g.next();!d.done;d=g.next())d=d.value,b.D[d]=a[d];a=R("SERVER_NAME",void 0);g=R("SERVER_VERSION",void 0);a&&g&&(b.D["server.name"]=a,b.D["server.version"]=g)}ff(R("ECATCHER_REPORT_HOST","")+"/error_204",
b);wi.add(c.message);xi++}}}
function Bi(a,b,c,d){c+="."+a;a=String(JSON.stringify(b)).substr(0,500);d[c]=a;return c.length+a.length}
;function Ci(){this.g=!1;this.f=null}
Ci.prototype.initialize=function(a,b,c,d,e,f){var g=this;f=void 0===f?!1:f;b?(this.g=!0,Mf(b,function(){g.g=!1;window.botguard?Di(g,c,d,f):(Rf(b),zi(new qi("Unable to load Botguard","from "+b)))},e)):a&&(eval(a),window.botguard?Di(this,c,d,f):zi(Error("Unable to load Botguard from JS")))};
function Di(a,b,c,d){if(d)try{a.f=new window.botguard.bg(b,c?function(){return c(b)}:Ha)}catch(e){zi(e)}else{try{a.f=new window.botguard.bg(b)}catch(e){zi(e)}c&&c(b)}}
Ci.prototype.dispose=function(){this.f=null};var Ei=new Ci;function Fi(){return!!Ei.f}
function Gi(a){a=void 0===a?{}:a;a=void 0===a?{}:a;return Ei.f?Ei.f.invoke(void 0,void 0,a):null}
;var Hi=E().toString();
function Ii(){a:{if(window.crypto&&window.crypto.getRandomValues)try{var a=Array(16),b=new Uint8Array(16);window.crypto.getRandomValues(b);for(var c=0;c<a.length;c++)a[c]=b[c];var d=a;break a}catch(e){}d=Array(16);for(a=0;16>a;a++){b=E();for(c=0;c<b%23;c++)d[a]=Math.random();d[a]=Math.floor(256*Math.random())}if(Hi)for(a=1,b=0;b<Hi.length;b++)d[a%16]=d[a%16]^d[(a-1)%16]/4^Hi.charCodeAt(b),a++}a=[];for(b=0;b<d.length;b++)a.push("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_".charAt(d[b]&63));
return a.join("")}
;var Ji=y.ytLoggingDocDocumentNonce_||Ii();z("ytLoggingDocDocumentNonce_",Ji,void 0);var Ki=1;function Li(a){this.f=a}
Li.prototype.getAsJson=function(){var a={};void 0!==this.f.trackingParams?a.trackingParams=this.f.trackingParams:(a.veType=this.f.veType,void 0!==this.f.veCounter&&(a.veCounter=this.f.veCounter),void 0!==this.f.elementIndex&&(a.elementIndex=this.f.elementIndex));void 0!==this.f.dataElement&&(a.dataElement=this.f.dataElement.getAsJson());void 0!==this.f.youtubeData&&(a.youtubeData=this.f.youtubeData);return a};
Li.prototype.toString=function(){return JSON.stringify(this.getAsJson())};
Li.prototype.isClientVe=function(){return!this.f.trackingParams&&!!this.f.veType};function Mi(a){a=void 0===a?0:a;return 0==a?"client-screen-nonce":"client-screen-nonce."+a}
function Ni(a){a=void 0===a?0:a;return 0==a?"ROOT_VE_TYPE":"ROOT_VE_TYPE."+a}
function Oi(a){return R(Ni(void 0===a?0:a),void 0)}
z("yt_logging_screen.getRootVeType",Oi,void 0);function Pi(){var a=Oi(0),b;a?b=new Li({veType:a,youtubeData:void 0}):b=null;return b}
function Qi(){var a=R("csn-to-ctt-auth-info");a||(a={},Q("csn-to-ctt-auth-info",a));return a}
function Ri(a){a=void 0===a?0:a;var b=R(Mi(a));if(!b&&!R("USE_CSN_FALLBACK",!0))return null;b||0!=a||(T("kevlar_client_side_screens")||T("c3_client_side_screens")?b="UNDEFINED_CSN":b=R("EVENT_ID"));return b?b:null}
z("yt_logging_screen.getCurrentCsn",Ri,void 0);function Si(a,b,c){var d=Qi();(c=Ri(c))&&delete d[c];b&&(d[a]=b)}
function Ti(a){return Qi()[a]}
z("yt_logging_screen.getCttAuthInfo",Ti,void 0);function Ui(a,b,c,d){c=void 0===c?0:c;if(a!==R(Mi(c))||b!==R(Ni(c)))if(Si(a,d,c),Q(Mi(c),a),Q(Ni(c),b),0==c||T("web_screen_associated_all_layers"))b=function(){setTimeout(function(){a&&Og("foregroundHeartbeatScreenAssociated",{clientDocumentNonce:Ji,clientScreenNonce:a},ri)},0)},"requestAnimationFrame"in window?window.requestAnimationFrame(b):b()}
z("yt_logging_screen.setCurrentScreen",Ui,void 0);function Vi(a,b,c){b=void 0===b?{}:b;c=void 0===c?!1:c;var d=R("EVENT_ID");d&&(b.ei||(b.ei=d));if(b){d=a;var e=void 0===e?!0:e;var f=R("VALID_SESSION_TEMPDATA_DOMAINS",[]),g=K(window.location.href);g&&f.push(g);g=K(d);if(0<=Ya(f,g)||!g&&0==d.lastIndexOf("/",0))if(T("autoescape_tempdata_url")&&(f=document.createElement("a"),Tb(f,d),d=f.href),d){g=d.match(Yb);d=g[5];f=g[6];g=g[7];var h="";d&&(h+=d);f&&(h+="?"+f);g&&(h+="#"+g);d=h;f=d.indexOf("#");if(d=0>f?d:d.substr(0,f))if(e&&!b.csn&&(b.itct||b.ved)&&
(b=Object.assign({csn:Ri()},b)),k){var k=parseInt(k,10);isFinite(k)&&0<k&&(e=b,b="ST-"+Xb(d).toString(36),e=e?ac(e):"",vf(b,e,k||5))}else k=b,e="ST-"+Xb(d).toString(36),k=k?ac(k):"",vf(e,k,5)}}if(c)return!1;if((window.ytspf||{}).enabled)spf.navigate(a);else{var l=void 0===l?{}:l;var m=void 0===m?"":m;var p=void 0===p?window:p;c=p.location;a=bc(a,l)+m;a=a instanceof I?a:Lb(a);c.href=Hb(a)}return!0}
;function Wi(a,b){this.version=a;this.args=b}
;function Xi(a,b){this.topic=a;this.f=b}
Xi.prototype.toString=function(){return this.topic};var Yi=B("ytPubsub2Pubsub2Instance")||new P;P.prototype.subscribe=P.prototype.subscribe;P.prototype.unsubscribeByKey=P.prototype.P;P.prototype.publish=P.prototype.O;P.prototype.clear=P.prototype.clear;z("ytPubsub2Pubsub2Instance",Yi,void 0);var Zi=B("ytPubsub2Pubsub2SubscribedKeys")||{};z("ytPubsub2Pubsub2SubscribedKeys",Zi,void 0);var $i=B("ytPubsub2Pubsub2TopicToKeys")||{};z("ytPubsub2Pubsub2TopicToKeys",$i,void 0);var aj=B("ytPubsub2Pubsub2IsAsync")||{};z("ytPubsub2Pubsub2IsAsync",aj,void 0);
z("ytPubsub2Pubsub2SkipSubKey",null,void 0);function bj(a,b){var c=cj();c&&c.publish.call(c,a.toString(),a,b)}
function dj(a){var b=ej,c=cj();if(!c)return 0;var d=c.subscribe(b.toString(),function(e,f){var g=B("ytPubsub2Pubsub2SkipSubKey");g&&g==d||(g=function(){if(Zi[d])try{if(f&&b instanceof Xi&&b!=e)try{var h=b.f,k=f;if(!k.args||!k.version)throw Error("yt.pubsub2.Data.deserialize(): serializedData is incomplete.");try{if(!h.J){var l=new h;h.J=l.version}var m=h.J}catch(p){}if(!m||k.version!=m)throw Error("yt.pubsub2.Data.deserialize(): serializedData version is incompatible.");try{f=Reflect.construct(h,
db(k.args))}catch(p){throw p.message="yt.pubsub2.Data.deserialize(): "+p.message,p;}}catch(p){throw p.message="yt.pubsub2.pubsub2 cross-binary conversion error for "+b.toString()+": "+p.message,p;}a.call(window,f)}catch(p){S(p)}},aj[b.toString()]?B("yt.scheduler.instance")?Wf(g):V(g,0):g())});
Zi[d]=!0;$i[b.toString()]||($i[b.toString()]=[]);$i[b.toString()].push(d);return d}
function fj(){var a=gj,b=dj(function(c){a.apply(void 0,arguments);hj(b)});
return b}
function hj(a){var b=cj();b&&("number"===typeof a&&(a=[a]),H(a,function(c){b.unsubscribeByKey(c);delete Zi[c]}))}
function cj(){return B("ytPubsub2Pubsub2Instance")}
;function ij(a){Wi.call(this,1,arguments);this.csn=a}
v(ij,Wi);var ej=new Xi("screen-created",ij),jj=[],kj=0;function lj(a,b,c){var d=T("use_default_events_client")?void 0:ri;b={csn:a,parentVe:b.getAsJson(),childVes:$a(c,function(f){return f.getAsJson()})};
c=u(c);for(var e=c.next();!e.done;e=c.next())e=e.value.getAsJson(),(jb(e)||!e.trackingParams&&!e.veType)&&zi(Error("Child VE logged with no data"));c={fa:Ti(a),S:a};"UNDEFINED_CSN"==a?mj("visualElementAttached",b,c):d?Og("visualElementAttached",b,d,c):si("visualElementAttached",b,c)}
function mj(a,b,c){jj.push({payloadName:a,payload:b,options:c});kj||(kj=fj())}
function gj(a){if(jj){for(var b=u(jj),c=b.next();!c.done;c=b.next())c=c.value,c.payload&&(c.payload.csn=a.csn,Og(c.payloadName,c.payload,null,c.options));jj.length=0}kj=0}
;function nj(a){a=a||{};var b={},c={};this.url=a.url||"";this.args=a.args||mb(b);this.assets=a.assets||{};this.attrs=a.attrs||mb(c);this.fallback=a.fallback||null;this.fallbackMessage=a.fallbackMessage||null;this.html5=!!a.html5;this.disable=a.disable||{};this.loaded=!!a.loaded;this.messages=a.messages||{}}
nj.prototype.clone=function(){var a=new nj,b;for(b in this)if(this.hasOwnProperty(b)){var c=this[b];"object"==Ja(c)?a[b]=mb(c):a[b]=c}return a};function oj(){M.call(this);this.f=[]}
v(oj,M);oj.prototype.o=function(){for(;this.f.length;){var a=this.f.pop();a.target.removeEventListener(a.name,a.Ca)}M.prototype.o.call(this)};var pj=/cssbin\/(?:debug-)?([a-zA-Z0-9_-]+?)(?:-2x|-web|-rtl|-vfl|.css)/;function qj(a){a=a||"";if(window.spf){var b=a.match(pj);spf.style.load(a,b?b[1]:"",void 0)}else rj(a)}
function rj(a){var b=sj(a),c=document.getElementById(b),d=c&&yf(c,"loaded");d||c&&!d||(c=tj(a,b,function(){yf(c,"loaded")||(wf(c),Hf(b),V(Sa(If,b),0))}))}
function tj(a,b,c){var d=document.createElement("link");d.id=b;d.onload=function(){c&&setTimeout(c,0)};
a=Mc(a);d.rel="stylesheet";d.href=vb(a).toString();(document.getElementsByTagName("head")[0]||document.body).appendChild(d);return d}
function sj(a){var b=Ic(document,"A");Tb(b,new I(Fb,a));a=b.href.replace(/^[a-zA-Z]+:\/\//,"//");return"css-"+Xb(a)}
;function uj(a,b,c,d){M.call(this);var e=this;this.m=this.Z=a;this.W=b;this.u=!1;this.api={};this.X=this.F=null;this.G=new P;Tc(this,Sa(Uc,this.G));this.j={};this.T=this.Y=this.h=this.ea=this.f=null;this.K=!1;this.l=this.C=null;this.aa={};this.za=["onReady"];this.da=null;this.na=NaN;this.U={};this.i=d;vj(this);this.ba("WATCH_LATER_VIDEO_ADDED",this.Sa.bind(this));this.ba("WATCH_LATER_VIDEO_REMOVED",this.Ta.bind(this));this.ba("onAdAnnounce",this.Ba.bind(this));this.Aa=new oj(this);Tc(this,Sa(Uc,this.Aa));
this.V=0;c?this.V=V(function(){e.loadNewVideoConfig(c)},0):d&&(wj(this),xj(this))}
v(uj,M);n=uj.prototype;n.getId=function(){return this.W};
n.loadNewVideoConfig=function(a){if(!this.g){this.V&&(W(this.V),this.V=0);a instanceof nj||(a=new nj(a));this.ea=a;this.f=a.clone();wj(this);this.Y||(this.Y=yj(this,this.f.args.jsapicallback||"onYouTubePlayerReady"));this.f.args.jsapicallback=null;if(a=this.f.attrs.width)this.m.style.width=Zc(Number(a)||a);if(a=this.f.attrs.height)this.m.style.height=Zc(Number(a)||a);xj(this);this.u&&zj(this)}};
function wj(a){var b;a.i?b=a.i.rootElementId:b=a.f.attrs.id;a.h=b||a.h;"video-player"==a.h&&(a.h=a.W,a.f.attrs.id=a.W);a.m.id==a.h&&(a.h+="-player",a.f.attrs.id=a.h)}
n.Ga=function(){return this.ea};
function zj(a){a.f&&!a.f.loaded&&(a.f.loaded=!0,"0"!=a.f.args.autoplay?a.api.loadVideoByPlayerVars(a.f.args):a.api.cueVideoByPlayerVars(a.f.args))}
function Aj(a){var b=!0,c=Bj(a);c&&a.f&&(a=Cj(a),b=yf(c,"version")===a);return b&&!!B("yt.player.Application.create")}
function xj(a){if(!a.g&&!a.K){var b=Aj(a);if(b&&"html5"==(Bj(a)?"html5":null))a.T="html5",a.u||Dj(a);else if(Ej(a),a.T="html5",b&&a.l)a.Z.appendChild(a.l),Dj(a);else{a.f&&(a.f.loaded=!0);var c=!1;a.C=function(){c=!0;var d=Fj(a,"player_bootstrap_method")?B("yt.player.Application.createAlternate")||B("yt.player.Application.create"):B("yt.player.Application.create");var e=a.f?a.f.clone():void 0;d(a.Z,e,a.i);Dj(a)};
a.K=!0;b?a.C():(Mf(Cj(a),a.C),(b=a.i?a.i.cssUrl:a.f.assets.css)&&qj(b),Gj(a)&&!c&&z("yt.player.Application.create",null,void 0))}}}
function Bj(a){var b=Ec(a.h);!b&&a.m&&a.m.querySelector&&(b=a.m.querySelector("#"+a.h));return b}
function Dj(a){if(!a.g){var b=Bj(a),c=!1;b&&b.getApiInterface&&b.getApiInterface()&&(c=!0);c?(a.K=!1,!Fj(a,"html5_remove_not_servable_check_killswitch")&&b.isNotServable&&a.f&&b.isNotServable(a.f.args.video_id)||Hj(a)):a.na=V(function(){Dj(a)},50)}}
function Hj(a){vj(a);a.u=!0;var b=Bj(a);b.addEventListener&&(a.F=Ij(a,b,"addEventListener"));b.removeEventListener&&(a.X=Ij(a,b,"removeEventListener"));var c=b.getApiInterface();c=c.concat(b.getInternalApiInterface());for(var d=0;d<c.length;d++){var e=c[d];a.api[e]||(a.api[e]=Ij(a,b,e))}for(var f in a.j)a.F(f,a.j[f]);zj(a);a.Y&&a.Y(a.api);a.G.O("onReady",a.api)}
function Ij(a,b,c){var d=b[c];return function(){try{return a.da=null,d.apply(b,arguments)}catch(e){"sendAbandonmentPing"!=c&&(e.params=c,a.da=e,Ke(e))}}}
function vj(a){a.u=!1;if(a.X)for(var b in a.j)a.X(b,a.j[b]);for(var c in a.U)W(parseInt(c,10));a.U={};a.F=null;a.X=null;for(var d in a.api)a.api[d]=null;a.api.addEventListener=a.ba.bind(a);a.api.removeEventListener=a.Xa.bind(a);a.api.destroy=a.dispose.bind(a);a.api.getLastError=a.Ha.bind(a);a.api.getPlayerType=a.Ia.bind(a);a.api.getCurrentVideoConfig=a.Ga.bind(a);a.api.loadNewVideoConfig=a.loadNewVideoConfig.bind(a);a.api.isReady=a.Ra.bind(a)}
n.Ra=function(){return this.u};
n.ba=function(a,b){var c=this,d=yj(this,b);if(d){if(!(0<=Ya(this.za,a)||this.j[a])){var e=Jj(this,a);this.F&&this.F(a,e)}this.G.subscribe(a,d);"onReady"==a&&this.u&&V(function(){d(c.api)},0)}};
n.Xa=function(a,b){if(!this.g){var c=yj(this,b);c&&ke(this.G,a,c)}};
function yj(a,b){var c=b;if("string"==typeof b){if(a.aa[b])return a.aa[b];c=function(){var d=B(b);d&&d.apply(y,arguments)};
a.aa[b]=c}return c?c:null}
function Jj(a,b){var c="ytPlayer"+b+a.W;a.j[b]=c;y[c]=function(d){var e=V(function(){if(!a.g){a.G.O(b,d);var f=a.U,g=String(e);g in f&&delete f[g]}},0);
kb(a.U,String(e))};
return c}
n.Ba=function(a){Hf("a11y-announce",a)};
n.Sa=function(a){Hf("WATCH_LATER_VIDEO_ADDED",a)};
n.Ta=function(a){Hf("WATCH_LATER_VIDEO_REMOVED",a)};
n.Ia=function(){return this.T||(Bj(this)?"html5":null)};
n.Ha=function(){return this.da};
function Ej(a){a.cancel();vj(a);a.T=null;a.f&&(a.f.loaded=!1);var b=Bj(a);b&&(Aj(a)||!Gj(a)?a.l=b:(b&&b.destroy&&b.destroy(),a.l=null));for(a=a.Z;b=a.firstChild;)a.removeChild(b)}
n.cancel=function(){if(this.C){var a=Cj(this);Sf(a,this.C)}W(this.na);this.K=!1};
n.o=function(){Ej(this);if(this.l&&this.f&&this.l.destroy)try{this.l.destroy()}catch(b){S(b)}this.aa=null;for(var a in this.j)y[this.j[a]]=null;this.ea=this.f=this.api=null;delete this.Z;delete this.m;M.prototype.o.call(this)};
function Gj(a){return a.f&&a.f.args&&a.f.args.fflags?-1!=a.f.args.fflags.indexOf("player_destroy_old_version=true"):!1}
function Cj(a){return a.i?a.i.jsUrl:a.f.assets.js}
function Fj(a,b){if(a.i)var c=a.i.serializedExperimentFlags;else a.f&&a.f.args&&(c=a.f.args.fflags);return"true"==Le(c||"")[b]}
;var Kj={},Lj="player_uid_"+(1E9*Math.random()>>>0);
function Mj(a,b,c){var d="player";c=void 0===c?!0:c;var e;"string"===typeof d?e=Ec(d):e=d;d=e;e=Lj+"_"+Na(d);var f=Kj[e];if(f&&c)return(b&&b.serializedExperimentFlags?b.serializedExperimentFlags.includes("web_player_remove_playerproxy=true"):a&&a.args&&a.args.fflags&&a.args.fflags.includes("web_player_remove_playerproxy=true"))?f.api.loadVideoByPlayerVars(a.args||null):f.loadNewVideoConfig(a),f.api;f=new uj(d,e,a,b);Kj[e]=f;Hf("player-added",f.api);Tc(f,Sa(Nj,f));return f.api}
function Nj(a){delete Kj[a.getId()]}
;function Oj(a){return(0===a.search("cue")||0===a.search("load"))&&"loadModule"!==a}
function Pj(a,b,c){"string"===typeof a&&(a={mediaContentUrl:a,startSeconds:b,suggestedQuality:c});a:{if((b=a.mediaContentUrl)&&(b=/\/([ve]|embed)\/([^#?]+)/.exec(b))&&b[2]){b=b[2];break a}b=null}a.videoId=b;return Qj(a)}
function Qj(a,b,c){if("string"===typeof a)return{videoId:a,startSeconds:b,suggestedQuality:c};b=["endSeconds","startSeconds","mediaContentUrl","suggestedQuality","videoId"];c={};for(var d=0;d<b.length;d++){var e=b[d];a[e]&&(c[e]=a[e])}return c}
function Rj(a,b,c,d){if(Ma(a)&&!Array.isArray(a)){b="playlist list listType index startSeconds suggestedQuality".split(" ");c={};for(d=0;d<b.length;d++){var e=b[d];a[e]&&(c[e]=a[e])}return c}b={index:b,startSeconds:c,suggestedQuality:d};"string"===typeof a&&16===a.length?b.list="PL"+a:b.playlist=a;return b}
;function Sj(a){a=void 0===a?!1:a;M.call(this);this.f=new P(a);Tc(this,Sa(Uc,this.f))}
F(Sj,M);Sj.prototype.subscribe=function(a,b,c){return this.g?0:this.f.subscribe(a,b,c)};
Sj.prototype.j=function(a,b){this.g||this.f.O.apply(this.f,arguments)};function Tj(a,b,c){Sj.call(this);this.h=a;this.i=b;this.l=c}
v(Tj,Sj);function Uj(a,b,c){if(!a.g){var d=a.h;d.g||a.i!=d.f||(a={id:a.l,command:b},c&&(a.data=c),d.f.postMessage(Md(a),d.i))}}
Tj.prototype.o=function(){this.i=this.h=null;Sj.prototype.o.call(this)};function Vj(a){M.call(this);this.f=a;this.f.subscribe("command",this.xa,this);this.h={};this.j=!1}
v(Vj,M);n=Vj.prototype;n.start=function(){this.j||this.g||(this.j=!0,Uj(this.f,"RECEIVING"))};
n.xa=function(a,b,c){if(this.j&&!this.g){var d=b||{};switch(a){case "addEventListener":"string"===typeof d.event&&(a=d.event,a in this.h||(c=C(this.Za,this,a),this.h[a]=c,this.addEventListener(a,c)));break;case "removeEventListener":"string"===typeof d.event&&Wj(this,d.event);break;default:this.i.isReady()&&this.i.isExternalMethodAvailable(a,c||null)&&(b=Xj(a,b||{}),c=this.i.handleExternalCall(a,b,c||null),(c=Yj(a,c))&&this.j&&!this.g&&Uj(this.f,a,c))}}};
n.Za=function(a,b){this.j&&!this.g&&Uj(this.f,a,this.ha(a,b))};
n.ha=function(a,b){if(null!=b)return{value:b}};
function Wj(a,b){b in a.h&&(a.removeEventListener(b,a.h[b]),delete a.h[b])}
n.o=function(){var a=this.f;a.g||ke(a.f,"command",this.xa,this);this.f=null;for(var b in this.h)Wj(this,b);M.prototype.o.call(this)};function Zj(a,b){Vj.call(this,b);this.i=a;this.start()}
v(Zj,Vj);Zj.prototype.addEventListener=function(a,b){this.i.addEventListener(a,b)};
Zj.prototype.removeEventListener=function(a,b){this.i.removeEventListener(a,b)};
function Xj(a,b){switch(a){case "loadVideoById":return b=Qj(b),[b];case "cueVideoById":return b=Qj(b),[b];case "loadVideoByPlayerVars":return[b];case "cueVideoByPlayerVars":return[b];case "loadPlaylist":return b=Rj(b),[b];case "cuePlaylist":return b=Rj(b),[b];case "seekTo":return[b.seconds,b.allowSeekAhead];case "playVideoAt":return[b.index];case "setVolume":return[b.volume];case "setPlaybackQuality":return[b.suggestedQuality];case "setPlaybackRate":return[b.suggestedRate];case "setLoop":return[b.loopPlaylists];
case "setShuffle":return[b.shufflePlaylist];case "getOptions":return[b.module];case "getOption":return[b.module,b.option];case "setOption":return[b.module,b.option,b.value];case "handleGlobalKeyDown":return[b.keyCode,b.shiftKey,b.ctrlKey,b.altKey,b.metaKey,b.key,b.code]}return[]}
function Yj(a,b){switch(a){case "isMuted":return{muted:b};case "getVolume":return{volume:b};case "getPlaybackRate":return{playbackRate:b};case "getAvailablePlaybackRates":return{availablePlaybackRates:b};case "getVideoLoadedFraction":return{videoLoadedFraction:b};case "getPlayerState":return{playerState:b};case "getCurrentTime":return{currentTime:b};case "getPlaybackQuality":return{playbackQuality:b};case "getAvailableQualityLevels":return{availableQualityLevels:b};case "getDuration":return{duration:b};
case "getVideoUrl":return{videoUrl:b};case "getVideoEmbedCode":return{videoEmbedCode:b};case "getPlaylist":return{playlist:b};case "getPlaylistIndex":return{playlistIndex:b};case "getOptions":return{options:b};case "getOption":return{option:b}}}
Zj.prototype.ha=function(a,b){switch(a){case "onReady":return;case "onStateChange":return{playerState:b};case "onPlaybackQualityChange":return{playbackQuality:b};case "onPlaybackRateChange":return{playbackRate:b};case "onError":return{errorCode:b}}return Vj.prototype.ha.call(this,a,b)};
Zj.prototype.o=function(){Vj.prototype.o.call(this);delete this.i};function ak(a,b,c){M.call(this);var d=this;c=c||R("POST_MESSAGE_ORIGIN",void 0)||window.document.location.protocol+"//"+window.document.location.hostname;this.h=b||null;this.u="*";this.i=c;this.sessionId=null;this.channel="widget";this.C=!!a;this.m=function(e){a:if(!("*"!=d.i&&e.origin!=d.i||d.h&&e.source!=d.h||"string"!==typeof e.data)){try{var f=JSON.parse(e.data)}catch(g){break a}if(!(null==f||d.C&&(d.sessionId&&d.sessionId!=f.id||d.channel&&d.channel!=f.channel))&&f)switch(f.event){case "listening":"null"!=
e.origin&&(d.i=d.u=e.origin);d.h=e.source;d.sessionId=f.id;d.f&&(d.f(),d.f=null);break;case "command":d.j&&(!d.l||0<=Ya(d.l,f.func))&&d.j(f.func,f.args,e.origin)}}};
this.l=this.f=this.j=null;window.addEventListener("message",this.m)}
v(ak,M);ak.prototype.sendMessage=function(a,b){var c=b||this.h;if(c){this.sessionId&&(a.id=this.sessionId);this.channel&&(a.channel=this.channel);try{var d=JSON.stringify(a);c.postMessage(d,this.u)}catch(e){Ke(e)}}};
ak.prototype.o=function(){window.removeEventListener("message",this.m);M.prototype.o.call(this)};function bk(){var a=this.g=new ak(!!R("WIDGET_ID_ENFORCE")),b=C(this.Wa,this);a.j=b;a.l=null;this.g.channel="widget";if(a=R("WIDGET_ID"))this.g.sessionId=a;this.i=[];this.l=!1;this.j={}}
n=bk.prototype;n.Wa=function(a,b,c){"addEventListener"==a&&b?(a=b[0],this.j[a]||"onReady"==a||(this.addEventListener(a,ck(this,a)),this.j[a]=!0)):this.ta(a,b,c)};
n.ta=function(){};
function ck(a,b){return C(function(c){this.sendMessage(b,c)},a)}
n.addEventListener=function(){};
n.Fa=function(){this.l=!0;this.sendMessage("initialDelivery",this.ia());this.sendMessage("onReady");H(this.i,this.ya,this);this.i=[]};
n.ia=function(){return null};
function dk(a,b){a.sendMessage("infoDelivery",b)}
n.ya=function(a){this.l?this.g.sendMessage(a):this.i.push(a)};
n.sendMessage=function(a,b){this.ya({event:a,info:void 0==b?null:b})};
n.dispose=function(){this.g=null};function ek(a){bk.call(this);this.f=a;this.h=[];this.addEventListener("onReady",C(this.Ua,this));this.addEventListener("onVideoProgress",C(this.eb,this));this.addEventListener("onVolumeChange",C(this.fb,this));this.addEventListener("onApiChange",C(this.Ya,this));this.addEventListener("onPlaybackQualityChange",C(this.ab,this));this.addEventListener("onPlaybackRateChange",C(this.bb,this));this.addEventListener("onStateChange",C(this.cb,this));this.addEventListener("onWebglSettingsChanged",C(this.gb,
this))}
v(ek,bk);n=ek.prototype;n.ta=function(a,b,c){if(this.f.isExternalMethodAvailable(a,c)){b=b||[];if(0<b.length&&Oj(a)){var d=b;if(Ma(d[0])&&!Array.isArray(d[0]))d=d[0];else{var e={};switch(a){case "loadVideoById":case "cueVideoById":e=Qj.apply(window,d);break;case "loadVideoByUrl":case "cueVideoByUrl":e=Pj.apply(window,d);break;case "loadPlaylist":case "cuePlaylist":e=Rj.apply(window,d)}d=e}b.length=1;b[0]=d}this.f.handleExternalCall(a,b,c);Oj(a)&&dk(this,this.ia())}};
n.Ua=function(){var a=C(this.Fa,this);this.g.f=a};
n.addEventListener=function(a,b){this.h.push({eventType:a,listener:b});this.f.addEventListener(a,b)};
n.ia=function(){if(!this.f)return null;var a=this.f.getApiInterface();cb(a,"getVideoData");for(var b={apiInterface:a},c=0,d=a.length;c<d;c++){var e=a[c];if(0===e.search("get")||0===e.search("is")){var f=0;0===e.search("get")?f=3:0===e.search("is")&&(f=2);f=e.charAt(f).toLowerCase()+e.substr(f+1);try{var g=this.f[e]();b[f]=g}catch(h){}}}b.videoData=this.f.getVideoData();b.currentTimeLastUpdated_=E()/1E3;return b};
n.cb=function(a){a={playerState:a,currentTime:this.f.getCurrentTime(),duration:this.f.getDuration(),videoData:this.f.getVideoData(),videoStartBytes:0,videoBytesTotal:this.f.getVideoBytesTotal(),videoLoadedFraction:this.f.getVideoLoadedFraction(),playbackQuality:this.f.getPlaybackQuality(),availableQualityLevels:this.f.getAvailableQualityLevels(),currentTimeLastUpdated_:E()/1E3,playbackRate:this.f.getPlaybackRate(),mediaReferenceTime:this.f.getMediaReferenceTime()};this.f.getVideoUrl&&(a.videoUrl=
this.f.getVideoUrl());this.f.getVideoContentRect&&(a.videoContentRect=this.f.getVideoContentRect());this.f.getProgressState&&(a.progressState=this.f.getProgressState());this.f.getPlaylist&&(a.playlist=this.f.getPlaylist());this.f.getPlaylistIndex&&(a.playlistIndex=this.f.getPlaylistIndex());this.f.getStoryboardFormat&&(a.storyboardFormat=this.f.getStoryboardFormat());dk(this,a)};
n.ab=function(a){dk(this,{playbackQuality:a})};
n.bb=function(a){dk(this,{playbackRate:a})};
n.Ya=function(){for(var a=this.f.getOptions(),b={namespaces:a},c=0,d=a.length;c<d;c++){var e=a[c],f=this.f.getOptions(e);b[e]={options:f};for(var g=0,h=f.length;g<h;g++){var k=f[g],l=this.f.getOption(e,k);b[e][k]=l}}this.sendMessage("apiInfoDelivery",b)};
n.fb=function(){dk(this,{muted:this.f.isMuted(),volume:this.f.getVolume()})};
n.eb=function(a){a={currentTime:a,videoBytesLoaded:this.f.getVideoBytesLoaded(),videoLoadedFraction:this.f.getVideoLoadedFraction(),currentTimeLastUpdated_:E()/1E3,playbackRate:this.f.getPlaybackRate(),mediaReferenceTime:this.f.getMediaReferenceTime()};this.f.getProgressState&&(a.progressState=this.f.getProgressState());dk(this,a)};
n.gb=function(){var a={sphericalProperties:this.f.getSphericalProperties()};dk(this,a)};
n.dispose=function(){bk.prototype.dispose.call(this);for(var a=0;a<this.h.length;a++){var b=this.h[a];this.f.removeEventListener(b.eventType,b.listener)}this.h=[]};function fk(a,b,c){M.call(this);this.f=a;this.i=c;this.j=jg(window,"message",C(this.l,this));this.h=new Tj(this,a,b);Tc(this,Sa(Uc,this.h))}
v(fk,M);fk.prototype.l=function(a){var b;if(b=!this.g)if(b=a.origin==this.i)a:{b=this.f;do{b:{var c=a.source;do{if(c==b){c=!0;break b}if(c==c.parent)break;c=c.parent}while(null!=c);c=!1}if(c){b=!0;break a}b=b.opener}while(null!=b);b=!1}if(b&&(b=a.data,"string"===typeof b)){try{b=JSON.parse(b)}catch(d){return}b.command&&(c=this.h,c.g||c.j("command",b.command,b.data,a.origin))}};
fk.prototype.o=function(){kg(this.j);this.f=null;M.prototype.o.call(this)};function gk(){var a=mb(hk),b;return $d(new O(function(c,d){a.onSuccess=function(e){Xe(e)?c(e):d(new ik("Request failed, status="+(e&&"status"in e?e.status:-1),"net.badstatus",e))};
a.onError=function(e){d(new ik("Unknown request error","net.unknown",e))};
a.R=function(e){d(new ik("Request timed out","net.timeout",e))};
b=ff("//googleads.g.doubleclick.net/pagead/id",a)}),function(c){c instanceof ae&&b.abort();
return Yd(c)})}
function ik(a,b){G.call(this,a+", errorCode="+b);this.errorCode=b;this.name="PromiseAjaxError"}
v(ik,G);function jk(){this.g=0;this.f=null}
jk.prototype.then=function(a,b,c){return 1===this.g&&a?(a=a.call(c,this.f),Sd(a)?a:kk(a)):2===this.g&&b?(a=b.call(c,this.f),Sd(a)?a:lk(a)):this};
jk.prototype.getValue=function(){return this.f};
jk.prototype.$goog_Thenable=!0;function lk(a){var b=new jk;a=void 0===a?null:a;b.g=2;b.f=void 0===a?null:a;return b}
function kk(a){var b=new jk;a=void 0===a?null:a;b.g=1;b.f=void 0===a?null:a;return b}
;function mk(a){G.call(this,a.message||a.description||a.name);this.isMissing=a instanceof nk;this.isTimeout=a instanceof ik&&"net.timeout"==a.errorCode;this.isCanceled=a instanceof ae}
v(mk,G);mk.prototype.name="BiscottiError";function nk(){G.call(this,"Biscotti ID is missing from server")}
v(nk,G);nk.prototype.name="BiscottiMissingError";var hk={format:"RAW",method:"GET",timeout:5E3,withCredentials:!0},ok=null;
function Fe(){if(T("disable_biscotti_fetch_on_html5_clients"))return Yd(Error("Fetching biscotti ID is disabled."));if(T("condition_biscotti_fetch_on_consent_cookie_html5_clients")&&!Ac.get("CONSENT","").startsWith("YES+"))return Yd(Error("User has not consented - not fetching biscotti id."));if("1"===gb(De(),"args","privembed"))return Yd(Error("Biscotti ID is not available in private embed mode"));ok||(ok=$d(gk().then(pk),function(a){return qk(2,a)}));
return ok}
function pk(a){a=a.responseText;if(0!=a.lastIndexOf(")]}'",0))throw new nk;a=JSON.parse(a.substr(4));if(1<(a.type||1))throw new nk;a=a.id;Ge(a);ok=kk(a);rk(18E5,2);return a}
function qk(a,b){var c=new mk(b);Ge("");ok=lk(c);0<a&&rk(12E4,a-1);throw c;}
function rk(a,b){V(function(){$d(gk().then(pk,function(c){return qk(b,c)}),Ha)},a)}
function sk(){try{var a=B("yt.ads.biscotti.getId_");return a?a():Fe()}catch(b){return Yd(b)}}
;function tk(a){if("1"!==gb(De(),"args","privembed")){a&&Ee();try{sk().then(function(){},function(){}),V(tk,18E5)}catch(b){S(b)}}}
;var Y=B("ytglobal.prefsUserPrefsPrefs_")||{};z("ytglobal.prefsUserPrefsPrefs_",Y,void 0);function uk(){this.f=R("ALT_PREF_COOKIE_NAME","PREF");var a=Ac.get(""+this.f,void 0);if(a){a=decodeURIComponent(a).split("&");for(var b=0;b<a.length;b++){var c=a[b].split("="),d=c[0];(c=c[1])&&(Y[d]=c.toString())}}}
n=uk.prototype;n.get=function(a,b){vk(a);wk(a);var c=void 0!==Y[a]?Y[a].toString():null;return null!=c?c:b?b:""};
n.set=function(a,b){vk(a);wk(a);if(null==b)throw Error("ExpectedNotNull");Y[a]=b.toString()};
n.remove=function(a){vk(a);wk(a);delete Y[a]};
n.save=function(){vf(this.f,this.dump(),63072E3)};
n.clear=function(){for(var a in Y)delete Y[a]};
n.dump=function(){var a=[],b;for(b in Y)a.push(b+"="+encodeURIComponent(String(Y[b])));return a.join("&")};
function wk(a){if(/^f([1-9][0-9]*)$/.test(a))throw Error("ExpectedRegexMatch: "+a);}
function vk(a){if(!/^\w+$/.test(a))throw Error("ExpectedRegexMismatch: "+a);}
function xk(a){a=void 0!==Y[a]?Y[a].toString():null;return null!=a&&/^[A-Fa-f0-9]+$/.test(a)?parseInt(a,16):null}
Ia(uk);function yk(a,b){for(var c=[],d=1;d<arguments.length;++d)c[d-1]=arguments[d];if(!zk(a)||c.some(function(e){return!zk(e)}))throw Error("Only objects may be merged.");
c=u(c);for(d=c.next();!d.done;d=c.next())Ak(a,d.value);return a}
function Ak(a,b){for(var c in b)if(zk(b[c])){if(c in a&&!zk(a[c]))throw Error("Cannot merge an object into a non-object.");c in a||(a[c]={});Ak(a[c],b[c])}else if(Bk(b[c])){if(c in a&&!Bk(a[c]))throw Error("Cannot merge an array into a non-array.");c in a||(a[c]=[]);Ck(a[c],b[c])}else a[c]=b[c];return a}
function Ck(a,b){for(var c=u(b),d=c.next();!d.done;d=c.next())d=d.value,zk(d)?a.push(Ak({},d)):Bk(d)?a.push(Ck([],d)):a.push(d);return a}
function zk(a){return"object"===typeof a&&!Array.isArray(a)}
function Bk(a){return"object"===typeof a&&Array.isArray(a)}
;function Dk(a,b){Wi.call(this,1,arguments)}
v(Dk,Wi);function Ek(a,b){Wi.call(this,1,arguments)}
v(Ek,Wi);var Fk=new Xi("aft-recorded",Dk),Gk=new Xi("timing-sent",Ek);var Hk=window;function Ik(){this.timing={};this.clearResourceTimings=function(){};
this.webkitClearResourceTimings=function(){};
this.mozClearResourceTimings=function(){};
this.msClearResourceTimings=function(){};
this.oClearResourceTimings=function(){}}
var Jk=Hk.performance||Hk.mozPerformance||Hk.msPerformance||Hk.webkitPerformance||new Ik;var Kk=!1;C(Jk.clearResourceTimings||Jk.webkitClearResourceTimings||Jk.mozClearResourceTimings||Jk.msClearResourceTimings||Jk.oClearResourceTimings||Ha,Jk);function Lk(a){var b=Mk(a);if(b.aft)return b.aft;a=R((a||"")+"TIMING_AFT_KEYS",["ol"]);for(var c=a.length,d=0;d<c;d++){var e=b[a[d]];if(e)return e}return NaN}
function Nk(a){var b;(b=B("ytcsi."+(a||"")+"data_"))||(b={tick:{},info:{}},Ta("ytcsi."+(a||"")+"data_",b));return b}
function Ok(a){a=Nk(a);a.info||(a.info={});return a.info}
function Mk(a){a=Nk(a);a.tick||(a.tick={});return a.tick}
function Pk(a){var b=Nk(a).nonce;b||(b=Ii(),Nk(a).nonce=b);return b}
function Qk(a){var b=Mk(a||""),c=Lk(a);c&&!Kk&&(bj(Fk,new Dk(Math.round(c-b._start),a)),Kk=!0)}
;function Rk(){var a=B("ytcsi.debug");a||(a=[],z("ytcsi.debug",a,void 0),z("ytcsi.reference",{},void 0));return a}
function Sk(a){a=a||"";var b=B("ytcsi.reference");b||(Rk(),b=B("ytcsi.reference"));if(b[a])return b[a];var c=Rk(),d={timerName:a,info:{},tick:{},span:{}};c.push(d);return b[a]=d}
;var Tk=y.ytLoggingLatencyUsageStats_||{};z("ytLoggingLatencyUsageStats_",Tk,void 0);function Uk(){this.f=0}
function Vk(){Uk.f||(Uk.f=new Uk);return Uk.f}
Uk.prototype.tick=function(a,b,c){Wk(this,"tick_"+a+"_"+b)||si("latencyActionTicked",{tickName:a,clientActionNonce:b},{timestamp:c})};
Uk.prototype.info=function(a,b){var c=Object.keys(a).join("");Wk(this,"info_"+c+"_"+b)||(c=Object.assign({},a),c.clientActionNonce=b,si("latencyActionInfo",c))};
Uk.prototype.span=function(a,b){var c=Object.keys(a).join("");Wk(this,"span_"+c+"_"+b)||(a.clientActionNonce=b,si("latencyActionSpan",a))};
function Wk(a,b){Tk[b]=Tk[b]||{count:0};var c=Tk[b];c.count++;c.time=X();a.f||(a.f=Uf(function(){var d=X(),e;for(e in Tk)Tk[e]&&6E4<d-Tk[e].time&&delete Tk[e];a&&(a.f=0)},5E3));
return 5<c.count?(6===c.count&&1>1E5*Math.random()&&(c=new qi("CSI data exceeded logging limit with key",b.split("_")),0<=b.indexOf("plev")||zi(c)),!0):!1}
;var Z={},Xk=(Z.ad_allowed="adTypesAllowed",Z.yt_abt="adBreakType",Z.ad_cpn="adClientPlaybackNonce",Z.ad_docid="adVideoId",Z.yt_ad_an="adNetworks",Z.ad_at="adType",Z.browse_id="browseId",Z.p="httpProtocol",Z.t="transportProtocol",Z.cpn="clientPlaybackNonce",Z.ccs="creatorInfo.creatorCanaryState",Z.cseg="creatorInfo.creatorSegment",Z.csn="clientScreenNonce",Z.docid="videoId",Z.GetHome_rid="requestIds",Z.GetSearch_rid="requestIds",Z.GetPlayer_rid="requestIds",Z.GetWatchNext_rid="requestIds",Z.GetBrowse_rid=
"requestIds",Z.GetLibrary_rid="requestIds",Z.is_continuation="isContinuation",Z.is_nav="isNavigation",Z.b_p="kabukiInfo.browseParams",Z.is_prefetch="kabukiInfo.isPrefetch",Z.is_secondary_nav="kabukiInfo.isSecondaryNav",Z.prev_browse_id="kabukiInfo.prevBrowseId",Z.query_source="kabukiInfo.querySource",Z.voz_type="kabukiInfo.vozType",Z.yt_lt="loadType",Z.mver="creatorInfo.measurementVersion",Z.yt_ad="isMonetized",Z.nr="webInfo.navigationReason",Z.nrsu="navigationRequestedSameUrl",Z.ncnp="webInfo.nonPreloadedNodeCount",
Z.pnt="performanceNavigationTiming",Z.prt="playbackRequiresTap",Z.plt="playerInfo.playbackType",Z.pis="playerInfo.playerInitializedState",Z.paused="playerInfo.isPausedOnLoad",Z.yt_pt="playerType",Z.fmt="playerInfo.itag",Z.yt_pl="watchInfo.isPlaylist",Z.yt_pre="playerInfo.preloadType",Z.yt_ad_pr="prerollAllowed",Z.pa="previousAction",Z.yt_red="isRedSubscriber",Z.rce="mwebInfo.responseContentEncoding",Z.scrh="screenHeight",Z.scrw="screenWidth",Z.st="serverTimeMs",Z.ssdm="shellStartupDurationMs",Z.aq=
"tvInfo.appQuality",Z.br_trs="tvInfo.bedrockTriggerState",Z.kebqat="kabukiInfo.earlyBrowseRequestInfo.abandonmentType",Z.kebqa="kabukiInfo.earlyBrowseRequestInfo.adopted",Z.label="tvInfo.label",Z.is_mdx="tvInfo.isMdx",Z.preloaded="tvInfo.isPreloaded",Z.upg_player_vis="playerInfo.visibilityState",Z.query="unpluggedInfo.query",Z.upg_chip_ids_string="unpluggedInfo.upgChipIdsString",Z.yt_vst="videoStreamType",Z.vph="viewportHeight",Z.vpw="viewportWidth",Z.yt_vis="isVisible",Z.rcl="mwebInfo.responseContentLength",
Z.GetSettings_rid="requestIds",Z.GetTrending_rid="requestIds",Z.GetMusicSearchSuggestions_rid="requestIds",Z.REQUEST_ID="requestIds",Z),Yk="isContinuation isNavigation kabukiInfo.earlyBrowseRequestInfo.adopted kabukiInfo.isPrefetch kabukiInfo.isSecondaryNav isMonetized navigationRequestedSameUrl performanceNavigationTiming playerInfo.isPausedOnLoad prerollAllowed isRedSubscriber tvInfo.isMdx tvInfo.isPreloaded isVisible watchInfo.isPlaylist playbackRequiresTap".split(" "),Zk={},$k=(Zk.ccs="CANARY_STATE_",
Zk.mver="MEASUREMENT_VERSION_",Zk.pis="PLAYER_INITIALIZED_STATE_",Zk.yt_pt="LATENCY_PLAYER_",Zk.pa="LATENCY_ACTION_",Zk.yt_vst="VIDEO_STREAM_TYPE_",Zk),al="all_vc ap c cver cbrand cmodel cplatform ctheme ei l_an l_mm plid srt yt_fss yt_li vpst vpni2 vpil2 icrc icrt pa GetAccountOverview_rid GetHistory_rid cmt d_vpct d_vpnfi d_vpni nsru pc pfa pfeh pftr pnc prerender psc rc start tcrt tcrc ssr vpr vps yt_abt yt_fn yt_fs yt_pft yt_pre yt_pt yt_pvis ytu_pvis yt_ref yt_sts tds".split(" ");
function bl(a){return!!R("FORCE_CSI_ON_GEL",!1)||T("csi_on_gel")||!!Nk(a).useGel}
function cl(a){a=Nk(a);if(!("gel"in a))a.gel={gelTicks:{},gelInfos:{}};else if(a.gel){var b=a.gel;b.gelInfos||(b.gelInfos={});b.gelTicks||(b.gelTicks={})}return a.gel}
;function dl(a,b,c){if(null!==b)if(Ok(c)[a]=b,bl(c)){var d=b;b=cl(c);if(b.gelInfos)b.gelInfos["info_"+a]=!0;else{var e={};b.gelInfos=(e["info_"+a]=!0,e)}if(a.match("_rid")){var f=a.split("_rid")[0];a="REQUEST_ID"}if(a in Xk){b=Xk[a];0<=Ya(Yk,b)&&(d=!!d);a in $k&&"string"===typeof d&&(d=$k[a]+d.toUpperCase());a=d;d=b.split(".");for(var g=e={},h=0;h<d.length-1;h++){var k=d[h];g[k]={};g=g[k]}g[d[d.length-1]]="requestIds"===b?[{id:a,endpoint:f}]:a;f=yk({},e)}else 0<=Ya(al,a)||zi(new qi("Unknown label logged with GEL CSI",
a)),f=void 0;f&&bl(c)&&(b=Sk(c||""),yk(b.info,f),b=cl(c),"gelInfos"in b||(b.gelInfos={}),yk(b.gelInfos,f),c=Pk(c),Vk().info(f,c))}else Sk(c||"").info[a]=b}
function el(a,b,c){var d=Mk(c);if(T("use_first_tick")&&fl(a,c))return d[a];if(!b&&"_"!==a[0]){var e=a;Jk.mark&&(0==e.lastIndexOf("mark_",0)||(e="mark_"+e),c&&(e+=" ("+c+")"),Jk.mark(e))}e=b||X();d[a]=e;e=cl(c);e.gelTicks&&(e.gelTicks["tick_"+a]=!0);c||b||X();if(bl(c)){Sk(c||"").tick[a]=b||X();e=Pk(c);if("_start"===a){var f=Vk();Wk(f,"baseline_"+e)||si("latencyActionBaselined",{clientActionNonce:e},{timestamp:b})}else Vk().tick(a,e,b);Qk(c);e=!0}else e=!1;if(!e){if(!B("yt.timing."+(c||"")+"pingSent_")&&
(f=R((c||"")+"TIMING_ACTION",void 0),e=Mk(c),B("ytglobal.timing"+(c||"")+"ready_")&&f&&fl("_start")&&Lk(c)))if(Qk(c),c)gl(c);else{f=!0;var g=R("TIMING_WAIT",[]);if(g.length)for(var h=0,k=g.length;h<k;++h)if(!(g[h]in e)){f=!1;break}f&&gl(c)}Sk(c||"").tick[a]=b||X()}return d[a]}
function fl(a,b){var c=Mk(b);return a in c}
function gl(a){if(!bl(a)){var b=Mk(a),c=Ok(a),d=b._start,e=R("CSI_SERVICE_NAME","youtube"),f={v:2,s:e,action:R((a||"")+"TIMING_ACTION",void 0)},g=c.srt;void 0!==b.srt&&delete c.srt;b.aft=Lk(a);var h=Mk(a),k=h.pbr,l=h.vc;h=h.pbs;k&&l&&h&&k<l&&l<h&&Ok(a).yt_pvis&&"youtube"===e&&(dl("yt_lt","hot_bg",a),e=b.vc,k=b.pbs,delete b.aft,c.aft=Math.round(k-e));for(var m in c)"_"!==m.charAt(0)&&(f[m]=c[m]);b.ps=X();m={};e=[];for(var p in b)"_"!==p.charAt(0)&&(k=Math.round(b[p]-d),m[p]=k,e.push(p+"."+k));f.rt=
e.join(",");b=!!c.ap;T("debug_csi_data")&&(c=B("yt.timing.csiData"),c||(c=[],Ta("yt.timing.csiData",c)),c.push({page:location.href,time:new Date,args:f}));c="";for(var r in f)f.hasOwnProperty(r)&&(c+="&"+r+"="+f[r]);f="/csi_204?"+c.substring(1);if(window.navigator&&window.navigator.sendBeacon&&b){var q=void 0===q?"":q;rf(f,q)||qf(f,void 0,void 0,void 0,q)}else qf(f);z("yt.timing."+(a||"")+"pingSent_",!0,void 0);bj(Gk,new Ek(m.aft+(Number(g)||0),a))}}
var hl=window;hl.ytcsi&&(hl.ytcsi.info=dl,hl.ytcsi.tick=el);var il=null,jl=null,kl=null,ll={};function ml(a){var b=a.id;a=a.ve_type;var c=Ki++;a=new Li({veType:a,veCounter:c,elementIndex:void 0,dataElement:void 0,youtubeData:void 0});ll[b]=a;b=Ri();c=Pi();b&&c&&lj(b,c,[a])}
function nl(){var a=il.getVideoData(1);a=a.title?a.title+" - YouTube":"YouTube";document.title!==a&&(document.title=a)}
function ol(a){var b=a.csn;a=a.root_ve_type;if(b&&a&&(Ui(b,a),a=Pi()))for(var c in ll){var d=ll[c];d&&lj(b,a,[d])}}
function pl(a){ll[a.id]=new Li({trackingParams:a.tracking_params})}
function ql(a){var b=Ri(),c=ll[a.id];if(b&&c){a=T("use_default_events_client")?void 0:ri;var d="INTERACTION_LOGGING_GESTURE_TYPE_GENERIC_CLICK";c={csn:b,ve:c.getAsJson(),gestureType:d};d={fa:Ti(b),S:b};"UNDEFINED_CSN"==b?mj("visualElementGestured",c,d):a?Og("visualElementGestured",c,a,d):si("visualElementGestured",c,d)}}
function rl(a){a=a.ids;var b=Ri();if(b)for(var c=0;c<a.length;c++){var d=ll[a[c]];if(d){var e=b,f=T("use_default_events_client")?void 0:ri;d={csn:e,ve:d.getAsJson(),eventType:1};var g={fa:Ti(e),S:e};"UNDEFINED_CSN"==e?mj("visualElementShown",d,g):f?Og("visualElementShown",d,f,g):si("visualElementShown",d,g)}}}
;z("yt.setConfig",Q,void 0);z("yt.config.set",Q,void 0);z("yt.setMsg",uf,void 0);z("yt.msgs.set",uf,void 0);z("yt.logging.errors.log",Ai,void 0);
z("writeEmbed",function(){var a=R("PLAYER_CONFIG",void 0);if(!a){var b=R("PLAYER_VARS",void 0);b&&(a={args:b})}tk(!0);"gvn"==a.args.ps&&(document.body.style.backgroundColor="transparent");a.args.forced_experiments||(b=window.location.href,-1!=b.indexOf("?")?(b=(b||"").split("#")[0],b=b.split("?",2),b=Ne(1<b.length?b[1]:b[0])):b={},b.forced_experiments&&(a.args.forced_experiments=b.forced_experiments));a.attrs||(a.attrs={width:"100%",height:"100%",id:"video-player"});var c=document.referrer;b=R("POST_MESSAGE_ORIGIN");
window!=window.top&&c&&c!=document.URL&&(a.args.loaderUrl=c);il=a=(c=R("WEB_PLAYER_CONTEXT_CONFIGS",void 0))&&"WEB_PLAYER_CONTEXT_CONFIG_ID_EMBEDDED_PLAYER"in c?Mj(a,c.WEB_PLAYER_CONTEXT_CONFIG_ID_EMBEDDED_PLAYER,!1):Mj(a);a.addEventListener("onScreenChanged",ol);a.addEventListener("onLogClientVeCreated",ml);a.addEventListener("onLogServerVeCreated",pl);a.addEventListener("onLogVeClicked",ql);a.addEventListener("onLogVesShown",rl);a.addEventListener("onVideoDataChange",nl);c=R("POST_MESSAGE_ID","player");
R("ENABLE_JS_API")?kl=new ek(a):R("ENABLE_POST_API")&&"string"===typeof c&&"string"===typeof b&&(jl=new fk(window.parent,c,b),kl=new Zj(a,jl.h));ag()},void 0);
z("yt.www.watch.ads.restrictioncookie.spr",function(a){qf(a+"mac_204?action_fcts=1");return!0},void 0);
var sl=Je(function(){el("ol");var a=uk.getInstance(),b=!!((xk("f"+(Math.floor(119/31)+1))||0)&67108864),c=1<window.devicePixelRatio;if(document.body&&Kd(document.body,"exp-invert-logo"))if(c&&!Kd(document.body,"inverted-hdpi")){var d=document.body;if(d.classList)d.classList.add("inverted-hdpi");else if(!Kd(d,"inverted-hdpi")){var e=Id(d);Jd(d,e+(0<e.length?" inverted-hdpi":"inverted-hdpi"))}}else!c&&Kd(document.body,"inverted-hdpi")&&Ld();b!=c&&(b="f"+(Math.floor(119/31)+1),d=xk(b)||0,d=c?d|67108864:
d&-67108865,0==d?delete Y[b]:(c=d.toString(16),Y[b]=c.toString()),a.save())}),tl=Je(function(){var a=il;
a&&a.sendAbandonmentPing&&a.sendAbandonmentPing();R("PL_ATT")&&Ei.dispose();a=0;for(var b=Zf.length;a<b;a++)Yf(Zf[a]);Zf.length=0;Rf("//static.doubleclick.net/instream/ad_status.js");$f=!1;Q("DCLKSTAT",0);Vc(kl,jl);if(a=il)a.removeEventListener("onScreenChanged",ol),a.removeEventListener("onLogClientVeCreated",ml),a.removeEventListener("onLogServerVeCreated",pl),a.removeEventListener("onLogVeClicked",ql),a.removeEventListener("onLogVesShown",rl),a.removeEventListener("onVideoDataChange",nl),a.destroy();
ll={}});
window.addEventListener?(window.addEventListener("load",sl),window.addEventListener("unload",tl)):window.attachEvent&&(window.attachEvent("onload",sl),window.attachEvent("onunload",tl));Ta("yt.abuse.player.botguardInitialized",B("yt.abuse.player.botguardInitialized")||Fi);Ta("yt.abuse.player.invokeBotguard",B("yt.abuse.player.invokeBotguard")||Gi);Ta("yt.abuse.dclkstatus.checkDclkStatus",B("yt.abuse.dclkstatus.checkDclkStatus")||bg);
Ta("yt.player.exports.navigate",B("yt.player.exports.navigate")||Vi);Ta("yt.util.activity.init",B("yt.util.activity.init")||og);Ta("yt.util.activity.getTimeSinceActive",B("yt.util.activity.getTimeSinceActive")||rg);Ta("yt.util.activity.setTimestamp",B("yt.util.activity.setTimestamp")||pg);}).call(this);
