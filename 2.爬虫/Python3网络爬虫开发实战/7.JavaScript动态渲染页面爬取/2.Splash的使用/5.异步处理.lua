function main(splash, args)
    local example_urls = {"www.baidu.com", "www.taobao.com", "www.zhihu.com"}
    local urls = args.urls or example_urls
    local results = {}
    for index, url in ipairs(urls) do
        local ok, reason = splash:go("http://" .. url)
        if ok then
            splash:wait(2)
            results[url] = splash:png()
        end
    end
    return results
end