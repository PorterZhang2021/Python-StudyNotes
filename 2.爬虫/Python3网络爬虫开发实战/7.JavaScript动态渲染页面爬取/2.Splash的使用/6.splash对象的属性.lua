function main(splash, args)
    -- args属性用于获取页面加载时配置的参数
    local url = args.url 
    -- 等价操作
    local url = splash.args.url
    -- js_enabled属性
    splash:go("https://www.baidu.com")
    -- 禁止执行代码
    splash.js_enable=false
    local title = splash:evaljs("document.title")
    -- return {title=title}
    -- resource_timeout属性 用于检测是否超时
    splash.resource_timeout = 0.1
    assert(splash:go('https://www.taobao.com'))
    -- return splash:png()
    -- images_enable属性 设置是否加载图片，默认加载
    splash.images_enabled = false
    assert(splash:go('https://www.jd.com'))
    -- return{png=splash:png()}
    -- plugins_enabled属性 控制是否开启浏览器插件
    splash.plugins_enabled = true/false
    -- scroll-position属性 控制页面上下滚动或左右滚动
    assert(splash:go('https://www.taobao.com'))
    splash.scroll_position = {y=400}
    -- 页面左右滚动
    splash.scroll_position = {x=100, y=200}
    return {png=splash:png()}

end