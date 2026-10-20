<p align="center">
  <img src="https://raw.githubusercontent.com/ha-homelab/.github/main/assets/ha-homelab-logo.png" alt="HA Homelab: uma casa turquesa com nós de rede conectados" width="144" />
</p>

<h1 align="center">HA Homelab</h1>
<p align="center"><strong>Uma casa bem pensada. Automação compreensível.</strong></p>
<p align="center">
  <a href="https://ha-homelab.github.io/home-studio/install.html#native-studio">Instalar Home Studio no Home Assistant</a> ·
  <a href="https://github.com/ha-homelab/home-assistant">Explore a configuração</a> ·
  <a href="https://github.com/ha-homelab/.github/blob/main/community-tools/README.pt.md">Ferramentas da comunidade</a>
</p>

<!-- language-navigation:start -->
<p dir="ltr" align="center">
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.md" lang="en" dir="ltr">English</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ar.md" lang="ar" dir="rtl">العربية</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.bn.md" lang="bn" dir="ltr">বাংলা</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.cs.md" lang="cs" dir="ltr">Čeština</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.de.md" lang="de" dir="ltr">Deutsch</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.es.md" lang="es" dir="ltr">Español</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fa.md" lang="fa" dir="rtl">فارسی</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fr.md" lang="fr" dir="ltr">Français</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.he.md" lang="he" dir="rtl">עברית</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.hi.md" lang="hi" dir="ltr">हिन्दी</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.id.md" lang="id" dir="ltr">Bahasa Indonesia</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.it.md" lang="it" dir="ltr">Italiano</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ja.md" lang="ja" dir="ltr">日本語</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ko.md" lang="ko" dir="ltr">한국어</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.nl.md" lang="nl" dir="ltr">Nederlands</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pl.md" lang="pl" dir="ltr">Polski</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pt.md" lang="pt" dir="ltr">Português</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ru.md" lang="ru" dir="ltr">Русский</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.th.md" lang="th" dir="ltr">ไทย</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.tr.md" lang="tr" dir="ltr">Türkçe</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.uk.md" lang="uk" dir="ltr">Українська</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.vi.md" lang="vi" dir="ltr">Tiếng Việt</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hans.md" lang="zh-Hans" dir="ltr">简体中文</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hant.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

Criamos integrações do Home Assistant, clientes de voz, pontes para dispositivos,
ferramentas espaciais e guias de implantação reutilizáveis. Os projetos públicos
unem automação residencial prática a builds reproduzíveis, contratos explícitos
e recuperação documentada. Comece por um projeto: cada um tem seu próprio caminho
de instalação e hardware compatível.

![Papéis dos projetos HA Homelab: dispositivos, voz, configuração, ferramentas espaciais e testes](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/ecosystem.pt.svg)

O mapa agrupa trabalhos relacionados. Não significa que todos os projetos sejam
instalados juntos ou se integrem automaticamente uns aos outros.

## Novidades — outubro de 2026

- **Desenhe e publique sua casa diretamente no Home Assistant.** [Home Studio](https://ha-homelab.github.io/home-studio/install.html#native-studio) traz o editor 2D/3D, 206 modelos de móveis e jardim e 24 idiomas para dentro do HA. Desenhe cômodos, vincule áreas e dispositivos HA e escolha **Save draft**, depois **Publish family view**, para atualizar **3D Home**.
  [modo Dry run](https://github.com/ha-homelab/home-studio/blob/main/docs/dry-run.md) permite explorar a planta instalada bloqueando comandos para dispositivos.
  O [guia da primeira sessão](https://github.com/ha-homelab/home-studio/blob/main/docs/first-session.md) explica como começar com exemplos, recuperar rascunhos e preservar o trabalho quando o 3D não está disponível.
- **Mais formas de reutilizar o hardware existente.** [EchoMuse](https://github.com/ha-homelab/ha-echomuse) acrescenta um
  caminho documentado para voz, música e BLE no Echo Dot 2;
  [ZAC93 + ESP32](https://github.com/ha-homelab/zac93-esp32) documenta uma ponte Z-Wave. Os projetos RF, Zigbee e Tuya abaixo
  abrangem outras famílias de dispositivos. A prontidão do hardware varia por
  projeto: o comissionamento físico do ZAC93 ainda está pendente.
- **Configuração e recuperação públicas.** [Home Assistant](https://github.com/ha-homelab/home-assistant) agora inclui
  bibliotecas reutilizáveis de automações e scripts e contratos de integração;
  [k3s self-healing](https://github.com/ha-homelab/k3s-self-healing) publica ferramentas de implantação, backup e recuperação.
  Uma única instância com armazenamento local não oferece failover automático.
- **Evidências antes da automação.** Novos projetos de observação de sensores,
  direção de câmera e acesso acompanham quatro [ferramentas da comunidade](https://github.com/ha-homelab/.github/blob/main/community-tools/README.pt.md) para
  migração de entidades, procedência de medições, cenários de automação e resultados de voz.
  [DESLOC Lock Card](https://github.com/ha-homelab/ha-desloc-card) agora usa um botão adaptativo, mantendo a confirmação explícita de destravamento.

Este é um retrato editorial de **19 de outubro de 2026**. Consulte o README e as
versões de cada projeto para verificar compatibilidade e estado atuais.

## Instalar Home Studio no Home Assistant

Use **Home Assistant 2026.10 ou posterior** e uma conta de administrador.
Faça primeiro um backup do HA. Se já houver um **home_floorplan** gerado ou personalizado instalado, leia as [orientações de migração](https://github.com/ha-homelab/home-studio/blob/main/docs/home-assistant-editor.md#existing-generated-homes) antes de substituí-lo.

1. No HACS, adicione [`ha-homelab/home-studio`](https://github.com/ha-homelab/home-studio) como repositório personalizado da categoria **Integration**. Instale a versão estável mais recente que contenha **`home_floorplan.zip`**.
2. Reinicie o Home Assistant, abra **Settings → Devices & services → Add integration** e selecione **Home Studio**.
3. Abra **Home Studio** na barra lateral. Desenhe e mobílie um cômodo, vincule sua área e dispositivos HA e escolha **Save draft**.
4. Escolha **Publish family view** e abra **3D Home**. Verifique a planta e os vínculos com **Dry run** antes de ativar os controles dos dispositivos.

Uma instalação nativa nova não precisa de comandos Python, entrada YAML nem token API. O [guia de instalação nativa](https://ha-homelab.github.io/home-studio/install.html#native-studio) explica a configuração completa, a instalação manual do ZIP e o tratamento de instalações existentes.

## Explore os projetos

### Configuração e confiabilidade

- **[home-assistant](https://github.com/ha-homelab/home-assistant)** — configuração pública, automações e scripts incluídos,
  orientações de implantação e contratos de integração.
- **[k3s-self-healing](https://github.com/ha-homelab/k3s-self-healing)** — Home Assistant portátil em k3s, atualizações sujeitas
  a aprovação, backups verificados e ferramentas de recuperação.

### Voz e mídia

- **[asterisk-telephony](https://github.com/ha-homelab/asterisk-telephony)** — instalador verificado da integração Asterisk do projeto upstream, painéis para telefones SIP e controles de aparelhos Cisco, com um caminho de áudio separado para o Assist e resultados de aceitação documentados.
- **[ha-ottplay](https://github.com/ha-homelab/ha-ottplay)** — entidades de reprodutor de mídia e controle remoto do Home Assistant para players registrados por meio de um OTTPlay Control Server existente; os controles disponíveis dependem do player.
- **[ha-echomuse](https://github.com/ha-homelab/ha-echomuse)** — Echo Dot 2 com EchoMuse/emOS, Assist, música, ferramentas
  locais para a casa e um proxy BLE cadastrado separadamente. O caminho de
  reconhecimento de voz documentado usa um provedor de nuvem; não é totalmente offline.
  O piloto com palavra de ativação russa e Silero Baya não distribui os pesos privados do modelo.
- **[ha-echo-dot](https://github.com/ha-homelab/ha-echo-dot)** — conversão EchoLocal para Echo Dot 2, com ferramentas de
  treinamento da palavra de ativação e avaliação no ambiente exato de execução.
- **[ha-echo-show-5](https://github.com/ha-homelab/ha-echo-show-5)** — conversão do Echo Show 5 Gen2 para Android, backups
  verificados e configuração do Home Assistant Companion.
  Um teste ONNX opcional com uma única frase de ativação tem verificações de software; a aceitação acústica de ponta a ponta ainda está pendente.
- **[ha-lg-tv-capture](https://github.com/ha-homelab/ha-lg-tv-capture)** — ferramentas reutilizáveis de captura de tela LG webOS
  e integração com Home Assistant.

EchoLocal e EchoMuse são caminhos de conversão distintos. Leia os requisitos de
modelo e recuperação do projeto escolhido antes de modificar um dispositivo.

### Integrações, pontes e recuperação de dispositivos

- **[ha-radio-hub](https://github.com/ha-homelab/ha-radio-hub)** — protótipo PoE modular atual MC2-C + FH1 com três antenas externas independentes para Zigbee, Thread e Bluetooth, um Thread Border Router local, Z-Wave, RF de 433 MHz e sensores. Inclui CAD, firmware e ferramentas de implantação; a validação física ainda está pendente.
- **[ha-desloc](https://github.com/ha-homelab/ha-desloc)** — integração não oficial com a nuvem DESLOC para estado da
  fechadura, controles, bateria e Wi-Fi; [a compatibilidade varia conforme o modelo](https://github.com/ha-homelab/ha-desloc/blob/main/docs/compatibility.md).
- **[ha-desloc-card](https://github.com/ha-homelab/ha-desloc-card)** — cartão de painel separado com editor visual, ação
  adaptativa e comandos de destravamento com confirmação.
- **[rf-airbridge](https://github.com/ha-homelab/rf-airbridge)** — gateway ESPHome CC1101 para observações RF via MQTT,
  transmissão nativa ESPHome e automação no Home Assistant.
- **[zigbee-direct-button](https://github.com/ha-homelab/zigbee-direct-button)** — firmware para botões Tuya com controle nativo
  de grupos Zigbee: toque breve para alternar e pressão longa para desligar;
  veja os [limites atuais da validação física](https://github.com/ha-homelab/zigbee-direct-button/blob/main/docs/validation.md).
- **[ha-tuya-esphome](https://github.com/ha-homelab/ha-tuya-esphome)** — conversão de tomadas ESP8266 antigas, estação Linux
  reproduzível para gravação de firmware e guias de ponte Matter.
- **[zac93-esp32](https://github.com/ha-homelab/zac93-esp32)** — projeto ilustrado de ponte Zooz ZAC93 para ESP32-WROOM/S3,
  ESPHome e Z-Wave JS.
- **[slzb-06-recovery](https://github.com/ha-homelab/slzb-06-recovery)** — backup, atualização e recuperação Ethernet legada
  do SLZB-06 original; o firmware principal e o de rádio são alvos separados.

### Espaços, observações de sensores e acesso

- **[home-studio](https://github.com/ha-homelab/home-studio)** — desenhar e mobiliar cômodos diretamente no Home Assistant, salvar rascunhos editáveis e publicar a visualização 3D Home.
- **[ruview-home-sensing](https://github.com/ha-homelab/ruview-home-sensing)** — coleta experimental de CSI, firmware de receptores, hipóteses de atividade e ferramentas de evidências de inferência; publica por meio de ruview-home-assistant e não comprova a precisão de detecção no mundo real.
- **[sensing-evidence-kit](https://github.com/ha-homelab/sensing-evidence-kit)** — registre, anote e compare observações com
  verificações explícitas de atualidade e relógio.
- **[ruview-home-assistant](https://github.com/ha-homelab/ruview-home-assistant)** — observações RuView por MQTT discovery,
  atualidade por nó e exemplos de reprodução sintética.
- **[ha-onvif-room-direction](https://github.com/ha-homelab/ha-onvif-room-direction)** — estimativas de área a partir da leitura da
  direção da câmera, setores configurados e verificações de atualidade.
- **[ha-access-session](https://github.com/ha-homelab/ha-access-session)** — sessões Cloudflare Access verificadas para painéis
  externos e tokens de curta duração por um gateway restrito. Mapeia um único
  administrador Home Assistant explicitamente configurado, com privilégios completos.
  O acesso autenticado opcional às capas dos reprodutores de mídia fica desativado por padrão.

Os exemplos de sensores descrevem observações e seus limites. Reprodução sintética
e direção de câmera não comprovam a precisão da detecção de ocupação no mundo real.

### Testes e contratos

- **[ha-entity-migrations](https://github.com/ha-homelab/ha-entity-migrations)** — planos offline de migração semântica que
  distinguem a função de um dispositivo de seu hardware.
- **[ha-meter-contracts](https://github.com/ha-homelab/ha-meter-contracts)** — verificações de abrangência da medição,
  procedência, evidências de calibração e agregação.
- **[ha-scenario-tests](https://github.com/ha-homelab/ha-scenario-tests)** — cenários sintéticos delimitados em um mecanismo
  real e isolado de automação do Home Assistant.
- **[assist-scenario-lab](https://github.com/ha-homelab/assist-scenario-lab)** — evidências de voz offline que distinguem conclusão
  do protocolo, ação observada e resposta audível.

Siga o [fluxo ilustrado e seus resultados](https://github.com/ha-homelab/.github/blob/main/community-tools/process-and-results.pt.md). O seletor de idiomas do guia oferece todos os 24 idiomas.
Evidências de software e aceitação física permanecem etapas separadas.

<details>
<summary>Fluxo de revisão e verificações de software registradas</summary>

![Quatro ferramentas da comunidade e o limite da aceitação física separada](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/architecture.pt.svg)

![Contagens datadas dos testes Linux das quatro ferramentas, com notas separadas sobre testes ignorados](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/validation.pt.svg)

Estes diagramas preservam as [evidências de 16 de outubro de 2026 e as execuções de CI vinculadas no guia da comunidade](https://github.com/ha-homelab/.github/blob/main/community-tools/README.pt.md#validation-evidence--2026-10-16-utc).
As setas representam passagens de revisão. As contagens são evidências de software
com abrangência definida, não classificações de qualidade, percentuais de cobertura
ou benchmarks de dispositivos físicos.

</details>

## Veja em uso

<a href="https://ha-homelab.github.io/home-studio/install.html#native-studio">
  <img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/09-garage-studio.jpg" alt="Editor Home Studio no navegador com garagem, ateliê criativo e pátio fictícios em 3D" width="440" />
</a>
<a href="https://ha-homelab.github.io/home-studio/planner/guide.html">
  <img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/11-pattern-studio.jpg" alt="Editor Home Studio com um cômodo fictício, móveis, paletas de cores e padrões de superfície" width="440" />
</a>

**Home Studio:** Estas capturas existentes do editor separado mostram plantas fictícias: uma garagem com ateliê e um cômodo mobiliado com padrões. As mesmas ferramentas de desenho estão disponíveis dentro do HA.
[Instalar Home Studio no Home Assistant](https://ha-homelab.github.io/home-studio/install.html#native-studio) · [Guia ilustrado de desenho](https://ha-homelab.github.io/home-studio/planner/guide.html).
Home Studio contributors · MIT · [Fontes e procedência das imagens](https://github.com/ha-homelab/.github/blob/main/assets/profile/README.md).

### Opcional: desenhar fora do Home Assistant

O [planejador hospedado](https://ha-homelab.github.io/home-studio/planner/) continua útil durante a configuração ou solução de problemas do HA. Para desenhar offline, use uma cópia local baixada conforme o [guia do editor separado](https://github.com/ha-homelab/home-studio/blob/main/docs/home-assistant-editor.md). Esse editor não se conecta ao HA e mantém seu próprio rascunho no navegador. Transfira a planta manualmente com **Export JSON** e depois **Open JSON** no Home Studio dentro do HA; escolha **Save draft** e **Publish family view** quando estiver pronto.

Para outras visões dos projetos, explore a [arquitetura de voz, música e BLE do EchoMuse](https://github.com/ha-homelab/ha-echomuse/blob/main/docs/architecture.md),
os [diagramas de ligação do ZAC93](https://github.com/ha-homelab/zac93-esp32) e a [demonstração de reprodução sintética do RuView](https://github.com/ha-homelab/ruview-home-assistant#try-it-without-hardware).

## Retrato dos projetos públicos

![Gráfico de barras: dispositivos e pontes 8; espaços, sensores e acesso 6; voz e mídia 6; testes e contratos 4; configuração e confiabilidade 2](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/portfolio.pt.svg)

**26 projetos + este repositório de perfil = 27 repositórios públicos**, verificados
em 19 de outubro de 2026. Cada projeto tem uma categoria editorial; as contagens
não medem maturidade, uso ou desempenho. [Dados de origem reproduzíveis](https://github.com/ha-homelab/.github/blob/main/assets/profile/catalog.json).
Para resultados reais das verificações de software, veja o
[gráfico datado de testes das ferramentas da comunidade e as execuções de CI vinculadas](https://github.com/ha-homelab/.github/blob/main/community-tools/README.pt.md#validation-evidence--2026-10-16-utc).

## Projetos públicos relacionados fora desta organização

Estes projetos mantidos separadamente complementam o homelab. São componentes
opcionais, com configuração e limites de suporte próprios.

**Energia — [ecossistema Victron / Venus OS](https://github.com/victron-venus)**

- [inverter-climate](https://github.com/victron-venus/inverter-climate) coordena a climatização via Home Assistant e Venus OS,
  apenas observando por padrão.
- [dbus-emporia-vue](https://github.com/victron-venus/dbus-emporia-vue) expõe leituras de circuitos como cargas GX;
  [dbus-pump](https://github.com/victron-venus/dbus-pump) conecta entidades HA de reservatório, bomba e válvula.
- [inverter-dashboard-go](https://github.com/victron-venus/inverter-dashboard-go) oferece um painel de energia com interface Vue e
  dispositivos Home Assistant opcionais.

**Voz e mídia — incluindo o [ecossistema Open OTT Play](https://github.com/open-ott-play)**

- [Amazon Echo Home Energy](https://github.com/4alvit/amazon-echo-home-voice) é uma skill Alexa personalizada somente de leitura;
  [Google Home / Nest reports](https://github.com/4alvit/google-home-voice-stats) envia vídeo Cast com fala sintetizada localmente.
  Funcionam sem conversão de hardware; Home Assistant é opcional, e a skill Alexa não o exige.
- [EPG Voice Gateway](https://github.com/4alvit/epg-voice-gateway) encontra programas XMLTV atuais e encaminha a reprodução
  por um proxy HLS existente para telas Alexa ou Google Cast.
- [OTT-play Control Server](https://github.com/open-ott-play/ottplay-control-server) oferece comandos do player, controle por terminal
  e implantação em k3s. O gateway EPG não depende do OttPlay.
- [Cisco Home Telephony](https://github.com/4alvit/cisco-home-telephony) — provisionamento SIP para Cisco 7945G, Asterisk em k3s, CLI de telefonia e fluxos opcionais de voz e controle com Home Assistant.

**Infraestrutura reutilizável**

- [ESPHome BLE Sensor Patterns](https://github.com/4alvit/esphome-ble-sensor-patterns) oferece configurações ESP32 de referência
  para sensores de bateria, temperatura e plantas.
- [FastAPI MQTT Gateway](https://github.com/4alvit/fastapi-mqtt-gateway) conecta REST/WebSocket e MQTT com autenticação e
  restrições de tópicos.
- [MQTT Observability](https://github.com/4alvit/mqtt-observability-opentelemetry) observa métricas MQTT e Mosquitto via OpenTelemetry,
  Prometheus e Grafana; não é um proxy de mensagens.
- [HA Homelab Terraform](https://github.com/4alvit/terraform-github-ha-homelab) gerencia as configurações GitHub e os repositórios desta organização.
- [Venus OS CI Toolkit](https://github.com/victron-venus/venus-os-ci-toolkit) — workflows compartilhados do GitHub Actions e ferramentas de CI para validação, releases e verificações de segurança; os consumidores fixam um commit revisado.

## Como trabalhamos

Comportamento compreensível, alterações revisáveis, builds reproduzíveis e
recuperação documentada. Exemplos públicos e capturas usam dados sintéticos quando
indicado; credenciais domésticas, gravações, backups de dispositivos e exportações
operacionais privadas ficam fora destes repositórios. Cada projeto documenta o
que foi testado e o que ainda precisa de verificação física.

Contribua pelo guia do repositório correspondente; relate vulnerabilidades pela
política de segurança. Este repositório também contém nosso
[logotipo original e notas de design](https://github.com/ha-homelab/.github/blob/main/assets/README.md).

---

Um homelab independente criado com [Home Assistant](https://www.home-assistant.io/).
Sem afiliação com o projeto Home Assistant ou com fabricantes de dispositivos.
