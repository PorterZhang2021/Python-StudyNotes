function main(splash, args)
    -- go方法用于请求某个链接，可以模拟GET请求和POST请求
    -- 同时传入请求头，表单等数据
    -- local ok, reason = splash:go{"https://www.httpbin.org/post", http_method="POST", body="name=Germey"}
    -- if ok then
    --     return splash:html()
    -- end

    -- wait方法用于控制页面等待时间
    -- splash:go("https://www.taobao.com")
    -- splash:wait(2)
    -- return {html=splash:html()}

    -- jsfunc方法用于直接调用JavaScript定义的方法，但是需要用双中括号把调用的方法包起来
    -- local get_div_count = splash:jsfunc([[function(){
    --     var body = document.body;
    --     var divs = body.getElementsByTagName('div');
    --     return divs.length;
    -- }]])
    -- splash:go('https://www.baidu.com')
    -- return ("There are %s DIVs"):format(get_div_count())

    -- evaljs方法 执行JavaScript代码并返回最后一条JavaScript语句返回结果
    -- result = splash:evaljs(js)
    -- local title = splash:evaljs("document")

    -- runjs方法 用于执行JavaScript代码
    -- splash:go("https://www.baidu.com")
    -- splash:runjs("foo = function() {return 'bar'}")
    -- local result = splash:evaljs("foo()")
    -- return result

    -- html方法 用于获取页面的源代码
    -- splash:go("https://www.httpbin.org/get")
    -- return splash:html()

    -- png方法 用于获取png格式的页面截图
    -- splash:go("https://www.taobao.com")
    -- return splash:png()

    -- jpeg方法 获取JPEG格式的页面截图
    -- splash:go("https://www.taobao.com")
    -- return splash:jpeg()

    -- har方法 用于获取页面加载过程描述信息
    -- splash:go("https://www.baidu.com")
    -- return splash:har()

    -- url方法 用于获取当前正在访问的URL
    -- splash:go("https://www.baidu.com")
    -- return splash:url()

    -- set_user_agent方法
    -- 此方法用于设置浏览器的User-Agent头
    -- splash:set_user_agent('splash')
    -- splash:go("https://www.httpbin.org/get")
    -- return splash:html()

    -- select方法
    -- 用于选中符合条件的第一个节点，如果有多个节点符合条件则只返回一个
    -- splash:go("https://www.baidu.com/")
    -- input = splash:select("#kw")
    -- input:send_text('Splash')
    -- splash:wait(3)
    -- return splash:png()

    -- select_all方法
    -- 用于选中所有符合条件的节点，其参数是CSS选择器
    -- local treat = require('treat')
    -- assert(splash:go("https://quotes.toscrape.com/"))
    -- assert(splash:wait(0.5))
    -- local texts = splash:select_all('.quote .text')
    -- local results = {}
    -- for index, text in ipairs(texts) do
    --     results[index] = text.node.innerHTML
    -- end
    -- return treat.as_array(results)

    -- -- mouse_click方法
    -- splash:go("https://www.baidu.com/")
    -- input = splash:select("#kw")
    -- input:send_text('Splash')
    -- splash:wait(3)
    -- submit = splash:select('#su')
    -- submit:mouse_click()
    -- splash:wait(5)
    -- return splash:png()
end