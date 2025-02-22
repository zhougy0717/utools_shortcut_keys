class ShortcutList {

    constructor() {
        this._name = 'welink'
        this._appName = 'welinkpc'
        this._dir = __dirname
        this._shortcutData = [
        {
            title: '提取消息 ctrl + alt + z',
            description: '提取消息',
            keyword: 'windows tiqu xiaoxi msg welink espace',
            keys: ['z', "ctrl", "alt"],
            icon: 'icons/welink.png'
        },
        {
            title: '捕捉屏幕 ctrl + alt + a',
            description: '捕捉屏幕',
            keyword: 'windows buzhuo pingmu capture screen welink espace',
            keys: ['a', "ctrl", "alt"],
            icon: 'icons/welink.png'
        },
        {
            title: '消息翻译 alt + c',
            description: '消息翻译',
            keyword: 'windows xiaoxi fanyi msg translate welink espace',
            keys: ['c', "alt"],
            icon: 'icons/welink.png'
        },
        {
            title: '显示主界面 ctrl + alt + d',
            description: '显示主界面',
            keyword: 'windows show main xianshi welink espace',
            keys: ['d', "ctrl", "alt"],
            icon: 'icons/welink.png'
        },
        {
            title: '显示通话窗口（多窗口模式） alt + d',
            description: '显示通话窗口（多窗口模式）',
            keyword: 'windows show dialog chuangkou welink espace',
            keys: ['d', "alt"],
            icon: 'icons/welink.png'
        }] 
    }

    get() {
        for (let sc of this._shortcutData) {
            sc['keyword'] += ` ${this._name} ${this._appName}`
            sc['icon'] = `shortcuts/${this._name}/welink.png`
        }
        return this._shortcutData
    }

    name() {
        return `${this._name}`
    }
}

module.exports = new ShortcutList()
