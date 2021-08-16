# 蘋果八股測試

測試蘋果八股需要安裝 Beta schema 同埋 patch librime 去準確將候選詞排序.

測試暫時只 support Mac 同埋 Squirrel 0.15.2.

如要安裝測試版, 請開啓 terminal, 執行以下 command, 執行installer script:
- Installer script 需要 git.
- Installer 需要 `sudo` 先夠 permission patch librime.
```
curl https://raw.githubusercontent.com/alex-the-man/rime-cantonese-experiment/master/checkout-run.sh | bash
```

安裝完後請 logout 再 login (用以 restart Squirrel) 然後按menu redeploy Squirrel.
