import streamlit as st
import pandas as pd
import altair as alt

def render_topics(language):
    def chart_growth(title, series):
        df = pd.DataFrame({"Year": [2024, 2025, 2026, 2027, 2028]})
        for label, values in series.items():
            df[label] = values
        return alt.Chart(df).transform_fold(
            list(series.keys()), as_=['Type', 'Value']
        ).mark_line(point=True).encode(
            x='Year:O',
            y='Value:Q',
            color='Type:N'
        ).properties(title=title)

    topics_en = [
        {
            "title": "Swiss 3rd Pillar Explained (Säule 3a)",
            "summary": "The Swiss 3rd Pillar, or Säule 3a, is a voluntary retirement savings plan that allows Swiss residents to contribute annually and deduct it from their taxable income. This results in immediate tax savings. There are two main types of 3a accounts: those offered by banks and those by insurance companies. Bank-based 3a accounts offer more flexibility, allowing withdrawals under certain conditions like home purchases or leaving Switzerland. Insurance-based options often include life insurance but can lock you into fixed premiums. As of 2024, you can contribute up to CHF 7,056 annually (for salaried workers). Investments in 3a accounts can grow tax-deferred, making them an essential component of Swiss retirement planning.",
            "chart": chart_growth("Bank vs. Insurance 3a Growth", {
                "Bank": [100, 112, 126, 140, 155],
                "Insurance": [100, 108, 116, 124, 132]
            }),
            "link": "https://www.ch.ch/en/retirement/third-pillar/"
        },
        {
            "title": "How Krankenkasse Really Works",
            "summary": "Switzerland’s health insurance system, known as Krankenkasse, requires everyone to have basic coverage (LaMal). You can choose from various models like Telmed, HMO, or the standard model. Each model affects your premium and flexibility. Supplemental insurance (Zusatzversicherung) offers coverage for private hospital rooms or alternative medicine. By choosing a higher deductible (franchise), opting for Telmed or HMO, and comparing annually, you can save over CHF 1,000/year. Premiums vary by canton, age, and provider. Every November, you can switch providers without penalty, giving you a key opportunity to optimize your costs.",
            "chart": chart_growth("Annual Premium by Model Type", {
                "Standard": [4000, 4050, 4100, 4200, 4300],
                "Telmed": [3600, 3620, 3650, 3675, 3700],
                "HMO": [3500, 3525, 3550, 3575, 3600]
            }),
            "link": "https://www.ch.ch/en/health/health-insurance/"
        },
        {
            "title": "Investing in Switzerland 101",
            "summary": "Getting started with investing in Switzerland is easier than most think. You can begin with as little as CHF 100/month using a Swiss brokerage. The most common and beginner-friendly way to invest is through ETFs (Exchange-Traded Funds), which provide diversified exposure to the market. Compared to savings accounts that offer minimal interest, ETFs offer higher long-term returns—though with more risk. Investment platforms like Swissquote, TrueWealth, or VIAC are tailored for residents. Over time, investing consistently can outpace inflation and savings account returns.",
            "chart": chart_growth("ETF vs. Savings Growth", {
                "ETF": [100, 115, 135, 160, 190],
                "Savings": [100, 101, 102, 104, 106]
            }),
            "link": "https://www.finanztipp.ch/etf/"
        },
        {
            "title": "Tax Deductions You’re Probably Missing",
            "summary": "Many Swiss residents miss out on tax deductions they’re entitled to. The most common include Säule 3a contributions, commuting costs, work-from-home expenses, childcare, continuing education, and even donations. Depending on your canton, tax-saving strategies vary—Zurich, for example, allows generous travel expense deductions. For freelancers, additional deductions include office equipment and insurance premiums. Use online calculators or consult local tax guides to identify what you can claim. Filing taxes efficiently can mean hundreds or even thousands of francs saved annually.",
            "chart": chart_growth("Estimated Savings by Deduction Type (CHF)", {
                "Commuting": [0, 400, 400, 400, 400],
                "3a": [0, 1411, 1411, 1411, 1411],
                "Childcare": [0, 1200, 1200, 1200, 1200]
            }),
            "link": "https://www.ch.ch/en/taxes/deductions/"
        },
        {
            "title": "Monthly Budgeting in Switzerland",
            "summary": "A typical budget in Switzerland uses the 50/30/20 rule: 50% on needs (rent, food, insurance), 30% on wants (travel, leisure), and 20% on savings or debt repayment. This model must be adapted to Swiss high costs. For example, rent in Zurich may take up to 40% of your salary. Budgeting apps like YNAB, Revolut, or Swiss-specific apps like FinanceFox help track expenses. Creating categories and using automation (standing orders) improves long-term discipline.",
            "chart": chart_growth("Monthly Budget Allocation (CHF 5,000)", {
                "Needs": [2500, 2500, 2500, 2500, 2500],
                "Wants": [1500, 1500, 1500, 1500, 1500],
                "Savings": [1000, 1000, 1000, 1000, 1000]
            }),
            "link": "https://www.ch.ch/en/money-budget/"
        },
        {
            "title": "The True Cost of Living Alone in CH",
            "summary": "Living alone in Switzerland is a luxury that requires careful planning. Typical monthly costs include CHF 1,500–2,500 for rent (city-dependent), CHF 350 for health insurance, CHF 100 for public transport, CHF 400–600 for food, and CHF 50–100 for subscriptions. Total monthly cost often exceeds CHF 3,000. Budgeting and realistic income assessments are key before deciding to move out alone.",
            "chart": chart_growth("Monthly Living Costs Breakdown", {
                "Rent": [1800, 1800, 1850, 1900, 1950],
                "Health Insurance": [350, 355, 360, 370, 375],
                "Transport": [100, 105, 105, 110, 110]
            }),
            "link": "https://www.ch.ch/en/living/"
        },
        {
            "title": "Krankenkasse Change Deadline: What You Need to Know",
            "summary": "Swiss health insurance contracts can be changed yearly by sending notice by the end of November. This window allows you to compare and switch to cheaper providers. Use official tools like Priminfo or Comparis to compare premiums. Switching requires a written Kündigung (termination letter) and sometimes proof of new coverage. Missing this deadline can cost you hundreds in overpaid premiums.",
            "chart": chart_growth("Premium Difference by Provider", {
                "Provider A": [400, 410, 420, 430, 440],
                "Provider B": [380, 385, 390, 395, 400]
            }),
            "link": "https://www.ch.ch/en/health/health-insurance/change-insurance/"
        },
        {
            "title": "Pillar 3a: Bank or Insurance?",
            "summary": "Choosing between bank-based and insurance-based 3a accounts comes down to flexibility and returns. Banks allow more freedom with withdrawals and better investment options like ETF portfolios. Insurances offer bundled life cover but lock you in. Over 20 years, banks often yield better returns if invested wisely. Compare fees, risk profiles, and exit conditions before committing.",
            "chart": chart_growth("20-Year Return Comparison", {
                "Bank ETF": [100, 115, 135, 155, 180],
                "Insurance Policy": [100, 108, 116, 124, 132]
            }),
            "link": "https://www.moneyland.ch/en/3a-pillar-bank-or-insurance"
        },
        {
            "title": "Swiss Franc Stability & Investing",
            "summary": "The Swiss Franc (CHF) is known globally as a ‘safe haven’ currency. It maintains value during global crises, backed by the Swiss National Bank’s low inflation and strict monetary policy. Investors holding assets in CHF reduce exposure to currency volatility. This makes Switzerland an attractive base currency for international and conservative investors.",
            "chart": chart_growth("CHF vs. USD & EUR Stability Index", {
                "CHF": [100, 102, 103, 104, 106],
                "USD": [100, 98, 96, 95, 97],
                "EUR": [100, 99, 98, 97, 98]
            }),
            "link": "https://www.snb.ch/en/"
        },
        {
            "title": "Expats: How to Navigate Swiss Finance",
            "summary": "Moving to Switzerland comes with a steep financial learning curve. You must get mandatory health insurance within 3 months. Understanding pension (AHV, 2nd pillar), tax filing by canton, and setting up a local bank are also essential. Begin with a basic Krankenkasse, register with the Gemeinde, and use apps like TaxInfo or moneyland.ch to estimate your finances. Language barriers can make navigating the system harder, but structured info can save you time and money.",
            "chart": chart_growth("Steps for Newcomer Financial Setup", {
                "Health Insurance": [1, 2, 2, 2, 2],
                "Bank Setup": [1, 1, 2, 2, 2],
                "Tax Registration": [0, 1, 2, 2, 2]
            }),
            "link": "https://www.ch.ch/en/moving-to-switzerland/"
        }
    ]
    
    topics_de = [
        {
            "title": "Erläuterung der Schweizer 3. Säule (Säule 3a)",
            "summary": "Die Schweizer 3. Säule, oder Säule 3a, ist eine freiwillige Altersvorsorge, die es den Schweizern ermöglicht, jährlich Beiträge zu leisten und diese von ihrem steuerpflichtigen Einkommen abzuziehen. Dies führt zu sofortigen Steuervorteilen. Es gibt zwei Haupttypen von 3a-Konten: die von Banken und die von Versicherungsgesellschaften angebotenen. Bankbasierte 3a-Konten bieten mehr Flexibilität, da Abhebungen unter bestimmten Bedingungen, wie z. B. dem Kauf einer Immobilie oder dem Verlassen der Schweiz, erlaubt sind. Versicherungsbasierte Optionen beinhalten häufig Lebensversicherungen, können jedoch an feste Prämien gebunden sein. Ab 2024 können bis zu CHF 7.056 jährlich (für Angestellte) eingezahlt werden. Investitionen in 3a-Konten können steuerfrei wachsen, was sie zu einem wichtigen Bestandteil der Altersvorsorge in der Schweiz macht.",
            "chart": chart_growth("Wachstum von Bank vs. Versicherung 3a", {
                "Bank": [100, 112, 126, 140, 155],
                "Insurance": [100, 108, 116, 124, 132]
            }),
            "link": "https://www.ch.ch/de/alter/3-saeule/"
        },
        {
            "title": "Wie Krankenkasse wirklich funktioniert",
            "summary": "Das Schweizer Gesundheitssystem, die Krankenkasse, verlangt von jedem, dass er eine Grundversicherung (LaMal) abschließt. Sie können zwischen verschiedenen Modellen wie Telmed, HMO oder dem Standardmodell wählen. Jedes Modell beeinflusst Ihre Prämie und Flexibilität. Zusätzliche Versicherungen bieten Deckung für private Krankenzimmer oder alternative Medizin. Durch die Wahl eines höheren Selbstbehalts (Franchise), die Wahl von Telmed oder HMO und einen jährlichen Vergleich können Sie über CHF 1.000 pro Jahr sparen. Die Prämien variieren je nach Kanton, Alter und Anbieter. Jedes Jahr im November können Sie den Anbieter ohne Strafgebühr wechseln, was eine wichtige Gelegenheit bietet, Ihre Kosten zu optimieren.",
            "chart": chart_growth("Jährliche Prämien nach Modelltyp", {
                "Standard": [4000, 4050, 4100, 4200, 4300],
                "Telmed": [3600, 3620, 3650, 3675, 3700],
                "HMO": [3500, 3525, 3550, 3575, 3600]
            }),
            "link": "https://www.ch.ch/de/gesundheit/krankenversicherung/"
        },
        {
            "title": "Investieren in der Schweiz 101",
            "summary": "Das Investieren in der Schweiz ist einfacher als die meisten denken. Sie können bereits mit nur CHF 100/Monat über eine Schweizer Brokerage beginnen. Die häufigste und anfängerfreundlichste Möglichkeit zu investieren, ist über ETFs (Exchange-Traded Funds), die eine diversifizierte Marktbetrachtung bieten. Im Vergleich zu Sparkonten, die nur geringe Zinsen bieten, bieten ETFs höhere langfristige Renditen – aber auch mehr Risiko. Investmentplattformen wie Swissquote, TrueWealth oder VIAC sind speziell für Einwohner der Schweiz zugeschnitten. Im Laufe der Zeit kann regelmäßiges Investieren die Inflation und die Renditen von Sparkonten übertreffen.",
            "chart": chart_growth("ETF vs. Sparen Wachstum", {
                "ETF": [100, 115, 135, 160, 190],
                "Savings": [100, 101, 102, 104, 106]
            }),
            "link": "https://www.finanztipp.ch/etf/"
        },
        {
            "title": "Steuerabzüge, die Sie wahrscheinlich verpassen",
            "summary": "Viele Schweizer verpassen Steuerabzüge, auf die sie Anspruch haben. Die häufigsten Abzüge sind Säule 3a-Beiträge, Pendelkosten, Heimarbeitskosten, Kinderbetreuung, Weiterbildung und sogar Spenden. Je nach Kanton variieren die Steuerstrategien – Zürich erlaubt beispielsweise großzügige Reisekostenabzüge. Für Freiberufler gibt es zusätzliche Abzüge wie Büroausstattung und Versicherungsprämien. Verwenden Sie Online-Rechner oder konsultieren Sie lokale Steuerführer, um herauszufinden, was Sie absetzen können. Eine effiziente Steuererklärung kann jährlich Hunderte oder sogar Tausende von Franken sparen.",
            "chart": chart_growth("Geschätzte Einsparungen nach Abzugstyp (CHF)", {
                "Pendeln": [0, 400, 400, 400, 400],
                "3a": [0, 1411, 1411, 1411, 1411],
                "Kinderbetreuung": [0, 1200, 1200, 1200, 1200]
            }),
            "link": "https://www.ch.ch/de/steuern/abzuege/"
        },
        {
            "title": "Wie Sie sich selbstständig machen (und Steuern sparen)",
            "summary": "Die Selbstständigkeit bietet enorme Vorteile, aber auch einige Herausforderungen. Die Schweiz hat ein flexibles System, das sowohl Einzelunternehmer als auch Freiberufler unterstützt. Sie müssen sich bei der AHV anmelden, eine Buchhaltung führen und Ihre Steuern erklären. Das Erstellen eines Businessplans, die Auswahl des richtigen rechtlichen Rahmens und das Einrichten einer Betriebsbuchhaltung sind entscheidend für den Erfolg. Zudem gibt es steuerliche Vorteile wie Abzüge für Büroausstattung, Reisekosten und Versicherungen. Denken Sie daran, dass das Steuersystem in der Schweiz kantonal unterschiedlich ist, sodass Sie Ihre Steuerstrategie gut planen sollten.",
            "chart": chart_growth("Selbstständigkeit vs. Angestelltengehalt (CHF)", {
                "Selbstständig": [3000, 3500, 4200, 5000, 6000],
                "Angestelltengehalt": [4000, 4100, 4200, 4300, 4400]
            }),
            "link": "https://www.ch.ch/de/selbstaendig-werden/"
        },
        {
            "title": "Der Weg zur finanziellen Unabhängigkeit",
            "summary": "Finanzielle Unabhängigkeit (FI) bedeutet, dass Ihr Einkommen aus Investitionen, passiven Einkommensquellen oder Unternehmen Ihre Lebenshaltungskosten deckt. In der Schweiz gibt es verschiedene Wege, dies zu erreichen, wie z.B. durch regelmäßiges Investieren in Immobilien oder Aktien und die Minimierung von Ausgaben. Die FI-Strategie beinhaltet langfristige Planung, das Erreichen von Einkommenszielen und das Streben nach finanzieller Freiheit, ohne auf ein monatliches Gehalt angewiesen zu sein. Für viele bedeutet dies, mindestens 25-mal den jährlichen Lebensunterhalt in einem Portfolio zu haben, das jährlich 4% an Rendite erzielt.",
            "chart": chart_growth("Wachstum des Portfolios zur FI (CHF)", {
                "Sparen": [100, 120, 145, 180, 220],
                "Investieren": [100, 130, 180, 250, 330]
            }),
            "link": "https://www.finanztipp.ch/finanzielle-unabhaengigkeit/"
        },
        {
            "title": "Kreditkarte vs. Debitkarte: Was ist besser?",
            "summary": "In der Schweiz gibt es eine Vielzahl von Zahlungsmethoden, aber Kreditkarten und Debitkarten sind die gängigsten. Kreditkarten bieten mehr Flexibilität und Belohnungen, jedoch mit höheren Gebühren und Zinsen. Debitkarten hingegen ziehen direkt vom Bankkonto ab und bieten in der Regel geringere Gebühren. Die Wahl zwischen Kreditkarte und Debitkarte hängt von Ihrem Ausgabeverhalten ab – bei regelmäßigen Ausgaben kann eine Kreditkarte vorteilhaft sein, während eine Debitkarte für diejenigen sinnvoller ist, die lieber nur das ausgeben, was sie bereits besitzen.",
            "chart": chart_growth("Kreditkartenbelohnungen vs. Gebühren", {
                "Belohnungen": [0, 50, 120, 200, 300],
                "Gebühren": [10, 25, 40, 60, 80]
            }),
            "link": "https://www.finanztipp.ch/kreditkarten-vs-debitkarten/"
        },
        {
            "title": "Die richtige Versicherung für Ihre Bedürfnisse wählen",
            "summary": "Versicherungen sind in der Schweiz ein wichtiger Bestandteil des finanziellen Schutzes. Es gibt verschiedene Arten von Versicherungen, darunter Lebensversicherungen, Krankenversicherungen, Haftpflicht- und Hausratversicherungen. Die Wahl der richtigen Versicherung hängt von Ihrer Lebenssituation, Ihrer Familie und Ihrem Job ab. Für junge Leute sind häufig nur Kranken- und Haftpflichtversicherungen notwendig, während Familien auch Lebens- und Hausratversicherungen benötigen. Achten Sie darauf, Ihre Versicherungen regelmäßig zu überprüfen und gegebenenfalls anzupassen.",
            "chart": chart_growth("Beliebte Versicherungsarten nach Altersgruppe", {
                "Krankenversicherung": [90, 90, 85, 80, 75],
                "Lebensversicherung": [30, 40, 50, 60, 70],
                "Hausratversicherung": [20, 30, 40, 50, 60]
            }),
            "link": "https://www.ch.ch/de/versicherungen/"
        },
        {
            "title": "Budgetierung und Schuldenmanagement in der Schweiz",
            "summary": "Budgetierung ist eine der wichtigsten Fähigkeiten, die jeder erlernen sollte, um in der Schweiz finanziell erfolgreich zu sein. Wenn Sie in der Schweiz leben, haben Sie möglicherweise mit hohen Lebenshaltungskosten, insbesondere in städtischen Gebieten, zu tun. Daher ist es wichtig, Ihre Ausgaben zu überwachen und Schulden zu vermeiden. Ein effektiver Haushaltsplan und Schuldenmanagement helfen, unerwartete Ausgaben zu bewältigen und langfristig zu sparen. Nutzen Sie Online-Budgeting-Tools und Apps, um Ihre Finanzen im Griff zu behalten.",
            "chart": chart_growth("Budgetierung vs. Schulden", {
                "Budgetiert": [100, 200, 300, 400, 500],
                "Schulden": [0, 50, 100, 150, 200]
            }),
            "link": "https://www.finanztipp.ch/budgetieren-und-schuldenmanagement/"
        },
        {
            "title": "Wie man Immobilien in der Schweiz kauft",
            "summary": "Der Kauf von Immobilien in der Schweiz ist ein komplexer, aber lohnender Prozess. Zunächst müssen Sie sich über Ihre Finanzierungsmöglichkeiten im Klaren sein – viele Menschen in der Schweiz benötigen einen Hypothekendarlehen, um den Kauf zu finanzieren. Der Kaufprozess umfasst die Suche nach der richtigen Immobilie, die Verhandlungen, die Durchführung von Due Diligence und die Überprüfung von Verträgen. Ein wichtiger Schritt ist es, zu verstehen, wie die Steuern auf Immobilien funktionieren und wie Sie langfristig von Ihrer Investition profitieren können.",
            "chart": chart_growth("Immobilienpreise in der Schweiz (pro Jahr)", {
                "Zürich": [5000, 5100, 5200, 5300, 5400],
                "Genf": [4500, 4600, 4700, 4800, 4900]
            }),
            "link": "https://www.finanztipp.ch/immobilienkauf-schweiz/"
        }
    ]
    
    topics_es = [
        {
            "title": "Explicación de la 3.ª Pilar Suizo (Pilar 3a)",
            "summary": "El Pilar 3, o Pilar 3a en Suiza, es un ahorro voluntario para la jubilación que permite a los suizos realizar aportaciones anuales y deducirlas de su ingreso imponible, lo que genera ventajas fiscales inmediatas. Existen dos tipos principales de cuentas 3a: las ofrecidas por bancos y las ofrecidas por compañías de seguros. Las cuentas 3a bancarias ofrecen más flexibilidad, ya que los retiros están permitidos bajo ciertas condiciones, como la compra de una propiedad o la salida de Suiza. Las opciones basadas en seguros a menudo incluyen seguros de vida, pero pueden estar atadas a primas fijas. A partir de 2024, se pueden aportar hasta CHF 7.056 anuales (para empleados). Las inversiones en cuentas 3a pueden crecer libre de impuestos, lo que las convierte en un componente clave del ahorro para la jubilación en Suiza.",
            "chart": chart_growth("Crecimiento de Banco vs. Seguro 3a", {
                "Banco": [100, 112, 126, 140, 155],
                "Seguro": [100, 108, 116, 124, 132]
            }),
            "link": "https://www.ch.ch/es/edad/3-saeule/"
        },
        {
            "title": "Cómo funciona realmente el seguro de salud",
            "summary": "El sistema de salud suizo, el seguro de salud, requiere que todos adquieran un seguro básico (LaMal). Los asegurados pueden elegir entre varios modelos como Telmed, HMO o el modelo estándar. Cada modelo influye en la prima y la flexibilidad. Los seguros adicionales ofrecen cobertura para habitaciones privadas o medicina alternativa. Al elegir una franquicia más alta, optar por Telmed o HMO y realizar una comparación anual, puedes ahorrar más de CHF 1.000 al año. Las primas varían según el cantón, la edad y el proveedor. Cada noviembre puedes cambiar de proveedor sin penalización, lo que es una oportunidad importante para optimizar tus costos.",
            "chart": chart_growth("Primas anuales según el tipo de modelo", {
                "Estándar": [4000, 4050, 4100, 4200, 4300],
                "Telmed": [3600, 3620, 3650, 3675, 3700],
                "HMO": [3500, 3525, 3550, 3575, 3600]
            }),
            "link": "https://www.ch.ch/es/salud/seguro-de-salud/"
        },
        {
            "title": "Invertir en Suiza 101",
            "summary": "Invertir en Suiza es más fácil de lo que muchos piensan. Puedes comenzar a invertir con solo CHF 100 al mes a través de una plataforma de corretaje suiza. La forma más común y amigable para los principiantes de invertir es a través de ETFs (fondos cotizados en bolsa), que ofrecen una visión diversificada del mercado. En comparación con las cuentas de ahorro, que ofrecen rendimientos bajos, los ETFs ofrecen rendimientos a largo plazo más altos, pero también más riesgo. Plataformas de inversión como Swissquote, TrueWealth o VIAC están diseñadas específicamente para los residentes en Suiza. Con el tiempo, invertir regularmente puede superar la inflación y los rendimientos de las cuentas de ahorro.",
            "chart": chart_growth("Crecimiento de ETF vs. Ahorros", {
                "ETF": [100, 115, 135, 160, 190],
                "Ahorros": [100, 101, 102, 104, 106]
            }),
            "link": "https://www.finanztipp.ch/etf/"
        },
        {
            "title": "Deducciones fiscales que probablemente estés perdiendo",
            "summary": "Muchos suizos pasan por alto las deducciones fiscales a las que tienen derecho. Las deducciones más comunes incluyen contribuciones al Pilar 3a, costos de transporte, costos de trabajo desde casa, cuidado de niños, educación continua e incluso donaciones. Dependiendo del cantón, las estrategias fiscales varían: por ejemplo, Zúrich permite deducciones generosas por costos de transporte. Los trabajadores autónomos tienen deducciones adicionales como equipo de oficina y primas de seguro. Utiliza calculadoras en línea o consulta guías fiscales locales para saber qué puedes deducir. Una declaración de impuestos eficiente puede ahorrarte cientos o incluso miles de francos cada año.",
            "chart": chart_growth("Ahorros estimados por tipo de deducción (CHF)", {
                "Transporte": [0, 400, 400, 400, 400],
                "3a": [0, 1411, 1411, 1411, 1411],
                "Cuidado de niños": [0, 1200, 1200, 1200, 1200]
            }),
            "link": "https://www.ch.ch/es/impuestos/deducciones/"
        },
        {
            "title": "Cómo iniciar tu propio negocio (y ahorrar impuestos)",
            "summary": "La autoempleo ofrece enormes beneficios, pero también algunos desafíos. Suiza tiene un sistema flexible que apoya tanto a los empresarios individuales como a los freelancers. Debes registrarte en la AHV, llevar una contabilidad y presentar tus impuestos. Crear un plan de negocios, elegir la estructura legal adecuada y configurar una contabilidad de operaciones son pasos cruciales para el éxito. Además, existen ventajas fiscales como deducciones por equipo de oficina, costos de viaje y seguros. Ten en cuenta que el sistema fiscal suizo varía de un cantón a otro, por lo que debes planificar bien tu estrategia fiscal.",
            "chart": chart_growth("Autoempleo vs. Salario (CHF)", {
                "Autoempleo": [3000, 3500, 4200, 5000, 6000],
                "Salario": [4000, 4100, 4200, 4300, 4400]
            }),
            "link": "https://www.ch.ch/es/autoempleo/"
        },
        {
            "title": "El camino hacia la independencia financiera",
            "summary": "La independencia financiera (IF) significa que tus ingresos provienen de inversiones, fuentes de ingresos pasivos o negocios, y cubren tus costos de vida. En Suiza, existen varias formas de alcanzar esta meta, como invertir regularmente en bienes raíces o acciones y minimizar los gastos. La estrategia de IF incluye una planificación a largo plazo, alcanzar objetivos de ingresos y lograr la libertad financiera sin depender de un salario mensual. Para muchos, esto significa tener un portafolio que sea al menos 25 veces su costo anual de vida, con un rendimiento anual del 4%.",
            "chart": chart_growth("Crecimiento de la cartera hacia la IF (CHF)", {
                "Ahorro": [100, 120, 145, 180, 220],
                "Inversión": [100, 130, 180, 250, 330]
            }),
            "link": "https://www.finanztipp.ch/independencia-financiera/"
        },
        {
            "title": "Tarjeta de crédito vs. tarjeta de débito: ¿Cuál es mejor?",
            "summary": "En Suiza, existen varios métodos de pago, pero las tarjetas de crédito y débito son los más comunes. Las tarjetas de crédito ofrecen más flexibilidad y recompensas, pero con tarifas y tasas de interés más altas. Las tarjetas de débito, por otro lado, descuentan directamente desde la cuenta bancaria y generalmente tienen tarifas más bajas. La elección entre tarjeta de crédito y débito depende de tus hábitos de gasto: las tarjetas de crédito pueden ser ventajosas para quienes tienen gastos regulares, mientras que las tarjetas de débito son más útiles para aquellos que prefieren gastar solo lo que ya tienen.",
            "chart": chart_growth("Recompensas vs. Tarifas de tarjetas de crédito", {
                "Recompensas": [0, 50, 120, 200, 300],
                "Tarifas": [10, 25, 40, 60, 80]
            }),
            "link": "https://www.finanztipp.ch/tarjetas-de-credito-vs-debito/"
        },
        {
            "title": "Elegir el seguro adecuado para tus necesidades",
            "summary": "Los seguros son una parte importante de la protección financiera en Suiza. Existen varios tipos de seguros, como seguros de vida, seguros de salud, responsabilidad civil y de propiedad. La elección del seguro adecuado depende de tu situación personal, tu familia y tu trabajo. Los jóvenes a menudo solo necesitan seguros de salud y responsabilidad civil, mientras que las familias pueden necesitar seguros de vida y de propiedad. Asegúrate de revisar regularmente tus seguros y ajustarlos si es necesario.",
            "chart": chart_growth("Tipos de seguros populares por grupo de edad", {
                "Seguro de salud": [90, 90, 85, 80, 75],
                "Seguro de vida": [30, 40, 50, 60, 70],
                "Seguro de propiedad": [20, 30, 40, 50, 60]
            }),
            "link": "https://www.ch.ch/es/seguros/"
        },
        {
            "title": "Presupuestar y gestionar deudas en Suiza",
            "summary": "El presupuesto es una de las habilidades más importantes que debes aprender para tener éxito financiero en Suiza. Si vives en Suiza, puedes enfrentarte a costos de vida elevados, especialmente en áreas urbanas. Por lo tanto, es crucial controlar tus gastos y evitar deudas. Un buen plan de presupuesto y gestión de deudas te ayudará a manejar gastos inesperados y ahorrar a largo plazo. Utiliza herramientas de presupuestación en línea y aplicaciones para mantener tus finanzas bajo control.",
            "chart": chart_growth("Presupuestar vs. Deudas", {
                "Presupuestado": [100, 200, 300, 400, 500],
                "Deudas": [0, 50, 100, 150, 200]
            }),
            "link": "https://www.finanztipp.ch/presupuesto-y-gestion-de-deudas/"
        },
        {
            "title": "Cómo comprar una propiedad en Suiza",
            "summary": "Comprar una propiedad en Suiza es un proceso complejo pero gratificante. Primero debes comprender tus opciones de financiamiento: la mayoría de las personas en Suiza necesitan un préstamo hipotecario para financiar la compra. El proceso de compra incluye encontrar la propiedad adecuada, negociar, realizar la debida diligencia y revisar los contratos. Un paso importante es entender cómo funcionan los impuestos sobre propiedades y cómo puedes beneficiarte a largo plazo de tu inversión.",
            "chart": chart_growth("Precios de propiedades en Suiza (por año)", {
                "Zúrich": [5000, 5100, 5200, 5300, 5400],
                "Ginebra": [4500, 4600, 4700, 4800, 4900]
            }),
            "link": "https://www.finanztipp.ch/comprar-propiedad-suiza/"
        }
    ]
    
    topics_fr = [
        {
            "title": "Explication du 3e Pilier Suisse (Pilier 3a)",
            "summary": "Le 3e Pilier, ou Pilier 3a, en Suisse, est une épargne volontaire pour la retraite qui permet aux Suisses de verser des cotisations annuelles et de les déduire de leur revenu imposable, ce qui génère des avantages fiscaux immédiats. Il existe deux types principaux de comptes 3a : ceux proposés par les banques et ceux proposés par les compagnies d'assurance. Les comptes 3a bancaires offrent plus de flexibilité, car les retraits sont autorisés sous certaines conditions, comme l'achat d'un bien immobilier ou le départ de la Suisse. Les options basées sur l'assurance incluent souvent des assurances-vie, mais peuvent être liées à des primes fixes. À partir de 2024, il est possible de verser jusqu'à 7 056 CHF par an (pour les salariés). Les investissements dans les comptes 3a peuvent croître sans impôt, ce qui en fait un élément clé de l'épargne retraite en Suisse.",
            "chart": chart_growth("Croissance de la Banque vs. Assurance 3a", {
                "Banque": [100, 112, 126, 140, 155],
                "Assurance": [100, 108, 116, 124, 132]
            }),
            "link": "https://www.ch.ch/fr/age/3e-pilier/"
        },
        {
            "title": "Comment fonctionne vraiment l'assurance maladie",
            "summary": "Le système de santé suisse, l'assurance maladie, exige que chaque personne souscrive une assurance de base (LaMal). Vous pouvez choisir entre différents modèles, tels que Telmed, HMO ou le modèle standard. Chaque modèle influence votre prime et votre flexibilité. Des assurances supplémentaires offrent une couverture pour les chambres privées ou la médecine alternative. En choisissant une franchise plus élevée, en optant pour Telmed ou HMO et en comparant annuellement, vous pouvez économiser plus de 1 000 CHF par an. Les primes varient en fonction du canton, de l'âge et du fournisseur. Chaque année en novembre, vous pouvez changer de fournisseur sans pénalité, ce qui est une occasion importante d'optimiser vos coûts.",
            "chart": chart_growth("Primes annuelles par type de modèle", {
                "Standard": [4000, 4050, 4100, 4200, 4300],
                "Telmed": [3600, 3620, 3650, 3675, 3700],
                "HMO": [3500, 3525, 3550, 3575, 3600]
            }),
            "link": "https://www.ch.ch/fr/sante/assurance-maladie/"
        },
        {
            "title": "Investir en Suisse 101",
            "summary": "Investir en Suisse est plus facile que ce que beaucoup pensent. Vous pouvez commencer à investir avec seulement 100 CHF par mois via une plateforme de courtage suisse. La manière la plus courante et la plus simple d'investir est par l'intermédiaire des ETF (fonds négociés en bourse), qui offrent une vue diversifiée du marché. Comparé aux comptes d'épargne, qui offrent de faibles rendements, les ETF offrent des rendements à long terme plus élevés, mais comportent également plus de risques. Des plateformes d'investissement telles que Swissquote, TrueWealth ou VIAC sont spécialement conçues pour les résidents suisses. Au fil du temps, un investissement régulier peut surpasser l'inflation et les rendements des comptes d'épargne.",
            "chart": chart_growth("Croissance des ETF vs. Épargne", {
                "ETF": [100, 115, 135, 160, 190],
                "Épargne": [100, 101, 102, 104, 106]
            }),
            "link": "https://www.finanztipp.ch/etf/"
        },
        {
            "title": "Déductions fiscales que vous ratez probablement",
            "summary": "Beaucoup de Suisses passent à côté des déductions fiscales auxquelles ils ont droit. Les déductions les plus courantes incluent les cotisations au Pilier 3a, les frais de transport, les frais de travail à domicile, la garde d'enfants, la formation continue et même les dons. En fonction du canton, les stratégies fiscales varient : par exemple, Zurich permet des déductions généreuses pour les frais de transport. Les travailleurs indépendants ont des déductions supplémentaires telles que l'équipement de bureau et les primes d'assurance. Utilisez des calculateurs en ligne ou consultez des guides fiscaux locaux pour savoir ce que vous pouvez déduire. Une déclaration fiscale efficace peut vous faire économiser des centaines, voire des milliers de francs chaque année.",
            "chart": chart_growth("Économies estimées par type de déduction (CHF)", {
                "Transport": [0, 400, 400, 400, 400],
                "3a": [0, 1411, 1411, 1411, 1411],
                "Garde d'enfants": [0, 1200, 1200, 1200, 1200]
            }),
            "link": "https://www.ch.ch/fr/impots/deductions/"
        },
        {
            "title": "Comment démarrer votre propre entreprise (et économiser des impôts)",
            "summary": "L'auto-entrepreneuriat offre d'énormes avantages, mais aussi quelques défis. La Suisse dispose d'un système flexible qui soutient à la fois les entrepreneurs individuels et les freelances. Vous devez vous inscrire à l'AVS, tenir une comptabilité et remplir vos déclarations fiscales. Créer un plan d'affaires, choisir la structure juridique appropriée et établir une comptabilité d'exploitation sont des étapes cruciales pour réussir. De plus, il existe des avantages fiscaux tels que des déductions pour le matériel de bureau, les frais de voyage et les assurances. Gardez à l'esprit que le système fiscal suisse varie d'un canton à l'autre, il est donc important de planifier soigneusement votre stratégie fiscale.",
            "chart": chart_growth("Auto-entrepreneur vs. Salaire (CHF)", {
                "Auto-entrepreneur": [3000, 3500, 4200, 5000, 6000],
                "Salaire": [4000, 4100, 4200, 4300, 4400]
            }),
            "link": "https://www.ch.ch/fr/auto-entrepreneur/"
        },
        {
            "title": "Le chemin vers l'indépendance financière",
            "summary": "L'indépendance financière (IF) signifie que vos revenus proviennent d'investissements, de sources de revenus passifs ou d'entreprises, et couvrent vos frais de subsistance. En Suisse, il existe plusieurs moyens d'atteindre cet objectif, tels que l'investissement régulier dans l'immobilier ou les actions et la réduction des dépenses. La stratégie IF inclut une planification à long terme, l'atteinte d'objectifs de revenus et l'obtention de la liberté financière sans dépendre d'un salaire mensuel. Pour beaucoup, cela signifie avoir un portefeuille d'investissement équivalant à au moins 25 fois leurs coûts de vie annuels, avec un rendement de 4% par an.",
            "chart": chart_growth("Croissance du portefeuille vers l'IF (CHF)", {
                "Épargne": [100, 120, 145, 180, 220],
                "Investissement": [100, 130, 180, 250, 330]
            }),
            "link": "https://www.finanztipp.ch/independance-financiere/"
        },
        {
            "title": "Carte de crédit vs. carte de débit : laquelle est la meilleure ?",
            "summary": "En Suisse, il existe plusieurs méthodes de paiement, mais les cartes de crédit et de débit sont les plus courantes. Les cartes de crédit offrent plus de flexibilité et de récompenses, mais avec des frais et des taux d'intérêt plus élevés. Les cartes de débit, en revanche, débitent directement votre compte bancaire et ont généralement des frais moins élevés. Le choix entre une carte de crédit et de débit dépend de vos habitudes de dépenses : les cartes de crédit peuvent être avantageuses pour ceux qui ont des dépenses régulières, tandis que les cartes de débit sont plus adaptées à ceux qui préfèrent ne dépenser que ce qu'ils ont déjà.",
            "chart": chart_growth("Récompenses vs. Frais des cartes de crédit", {
                "Récompenses": [0, 50, 120, 200, 300],
                "Frais": [10, 25, 40, 60, 80]
            }),
            "link": "https://www.finanztipp.ch/cartes-de-credit-vs-debit/"
        },
        {
            "title": "Choisir l'assurance adaptée à vos besoins",
            "summary": "Les assurances sont un élément important de la protection financière en Suisse. Il existe différents types d'assurances, telles que les assurances-vie, les assurances-maladie, responsabilité civile et biens. Le choix de l'assurance dépend de votre situation personnelle, de votre famille et de votre travail. Les jeunes ont souvent uniquement besoin d'une assurance-maladie et responsabilité civile, tandis que les familles peuvent avoir besoin d'assurances-vie et biens. Il est important de revoir régulièrement vos assurances et de les ajuster si nécessaire.",
            "chart": chart_growth("Types d'assurances populaires par groupe d'âge", {
                "Assurance-maladie": [90, 90, 85, 80, 75],
                "Assurance-vie": [30, 40, 50, 60, 70],
                "Assurance-biens": [20, 30, 40, 50, 60]
            }),
            "link": "https://www.ch.ch/fr/assurances/"
        },
        {
            "title": "Budgetiser et gérer les dettes en Suisse",
            "summary": "Le budget est l'une des compétences les plus importantes que vous devez apprendre pour réussir financièrement en Suisse. Si vous vivez en Suisse, vous pouvez être confronté à des coûts de la vie élevés, surtout dans les zones urbaines. Il est donc crucial de maîtriser vos dépenses et d'éviter les dettes. Un bon plan budgétaire et de gestion des dettes vous aidera à gérer les dépenses imprévues et à économiser à long terme. Utilisez des outils de budgétisation en ligne et des applications pour garder vos finances sous contrôle.",
            "chart": chart_growth("Budget vs. Dettes", {
                "Budget": [100, 200, 300, 400, 500],
                "Dettes": [0, 50, 100, 150, 200]
            }),
            "link": "https://www.finanztipp.ch/budgetisation-et-gestion-des-dettes/"
        },
        {
            "title": "Comment acheter un bien immobilier en Suisse",
            "summary": "Acheter un bien immobilier en Suisse est un processus complexe mais gratifiant. Vous devez d'abord comprendre vos options de financement : la plupart des gens en Suisse ont besoin d'un prêt hypothécaire pour financer l'achat. Le processus d'achat inclut la recherche de la propriété idéale, la négociation, la vérification de la diligence raisonnable et l'examen des contrats. Un élément clé est de comprendre comment fonctionnent les impôts fonciers et comment vous pouvez bénéficier à long terme de votre investissement.",
            "chart": chart_growth("Prix des propriétés en Suisse (par an)", {
                "Zurich": [5000, 5100, 5200, 5300, 5400],
                "Genève": [4500, 4600, 4700, 4800, 4900]
            }),
            "link": "https://www.finanztipp.ch/acheter-un-bien-immobilier-en-suisse/"
        }
    ]
    
    topics_it = [
        {
            "title": "Spiegazione del 3° Pilastro Svizzero (Pilastro 3a)",
            "summary": "Il 3° Pilastro, o Pilastro 3a, in Svizzera è una previdenza volontaria per la pensione che consente agli svizzeri di versare contributi annuali e di detrarli dal reddito imponibile, con vantaggi fiscali immediati. Esistono due tipi principali di conti 3a: quelli offerti dalle banche e quelli offerti dalle compagnie di assicurazione. I conti 3a bancari offrono maggiore flessibilità, in quanto i prelievi sono consentiti in determinate condizioni, come l'acquisto di un immobile o il trasferimento all'estero. Le opzioni basate sull'assicurazione spesso includono polizze vita, ma possono essere vincolate a premi fissi. A partire dal 2024, è possibile versare fino a 7.056 CHF all'anno (per i dipendenti). Gli investimenti nei conti 3a possono crescere senza essere tassati, il che li rende un elemento chiave della previdenza pensionistica in Svizzera.",
            "chart": chart_growth("Crescita della Banca vs. Assicurazione 3a", {
                "Banca": [100, 112, 126, 140, 155],
                "Assicurazione": [100, 108, 116, 124, 132]
            }),
            "link": "https://www.ch.ch/it/eta/3-pilastro/"
        },
        {
            "title": "Come funziona davvero l'assicurazione sanitaria",
            "summary": "Il sistema sanitario svizzero, l'assicurazione sanitaria, richiede che ogni persona sottoscriva un'assicurazione di base (LaMal). È possibile scegliere tra vari modelli, come Telmed, HMO o il modello standard. Ogni modello influisce sul premio e sulla flessibilità. Le assicurazioni aggiuntive offrono copertura per stanze private o medicina alternativa. Scegliendo una franchigia più alta, optando per Telmed o HMO e confrontando annualmente le offerte, è possibile risparmiare oltre 1.000 CHF all'anno. I premi variano in base al cantone, all'età e al fornitore. Ogni anno a novembre è possibile cambiare fornitore senza penale, un'opportunità importante per ottimizzare i costi.",
            "chart": chart_growth("Premi annuali per tipo di modello", {
                "Standard": [4000, 4050, 4100, 4200, 4300],
                "Telmed": [3600, 3620, 3650, 3675, 3700],
                "HMO": [3500, 3525, 3550, 3575, 3600]
            }),
            "link": "https://www.ch.ch/it/salute/assicurazione-sanitaria/"
        },
        {
            "title": "Investire in Svizzera 101",
            "summary": "Investire in Svizzera è più semplice di quanto molti pensino. Puoi iniziare a investire con soli 100 CHF al mese tramite una piattaforma di intermediazione svizzera. Il modo più comune e adatto ai principianti di investire è attraverso gli ETF (Exchange-Traded Funds), che offrono una visione diversificata del mercato. Rispetto ai conti di risparmio, che offrono bassi tassi di interesse, gli ETF offrono rendimenti più elevati nel lungo periodo, ma comportano anche più rischi. Piattaforme di investimento come Swissquote, TrueWealth o VIAC sono pensate appositamente per i residenti in Svizzera. Nel tempo, investire regolarmente può superare l'inflazione e i rendimenti dei conti di risparmio.",
            "chart": chart_growth("Crescita ETF vs. Risparmio", {
                "ETF": [100, 115, 135, 160, 190],
                "Risparmio": [100, 101, 102, 104, 106]
            }),
            "link": "https://www.finanztipp.ch/it/etf/"
        },
        {
            "title": "Detrazioni fiscali che probabilmente stai perdendo",
            "summary": "Molti svizzeri perdono le detrazioni fiscali a cui hanno diritto. Le detrazioni più comuni includono i contributi al Pilastro 3a, le spese per i trasporti, i costi per il lavoro a domicilio, la cura dei bambini, la formazione continua e anche le donazioni. A seconda del cantone, le strategie fiscali variano: ad esempio, Zurigo consente ampie detrazioni per le spese di trasporto. Per i liberi professionisti, ci sono ulteriori detrazioni come le attrezzature per l'ufficio e i premi assicurativi. Usa calcolatori online o consulta le guide fiscali locali per scoprire cosa puoi detrarre. Una dichiarazione fiscale efficiente può farti risparmiare centinaia o addirittura migliaia di franchi ogni anno.",
            "chart": chart_growth("Risparmi stimati per tipo di detrazione (CHF)", {
                "Trasporto": [0, 400, 400, 400, 400],
                "3a": [0, 1411, 1411, 1411, 1411],
                "Cura dei bambini": [0, 1200, 1200, 1200, 1200]
            }),
            "link": "https://www.ch.ch/it/tasse/detrazioni/"
        },
        {
            "title": "Come avviare la tua impresa (e risparmiare sulle tasse)",
            "summary": "L'imprenditoria offre enormi vantaggi, ma anche alcune sfide. La Svizzera ha un sistema flessibile che supporta sia gli imprenditori individuali che i liberi professionisti. Devi iscriverti all'AVS, tenere una contabilità e presentare le dichiarazioni fiscali. Creare un business plan, scegliere la struttura giuridica appropriata e gestire la contabilità operativa sono passaggi cruciali per il successo. Inoltre, esistono vantaggi fiscali come le detrazioni per attrezzature da ufficio, spese di viaggio e assicurazioni. Tieni presente che il sistema fiscale svizzero varia da cantone a cantone, quindi è importante pianificare attentamente la tua strategia fiscale.",
            "chart": chart_growth("Libero professionista vs. Stipendio (CHF)", {
                "Libero professionista": [3000, 3500, 4200, 5000, 6000],
                "Stipendio": [4000, 4100, 4200, 4300, 4400]
            }),
            "link": "https://www.ch.ch/it/libero-professionista/"
        },
        {
            "title": "Il percorso verso l'indipendenza finanziaria",
            "summary": "L'indipendenza finanziaria (IF) significa che i tuoi redditi provengono da investimenti, redditi passivi o imprese, coprendo i tuoi costi di vita. In Svizzera ci sono diversi modi per raggiungere questo obiettivo, come investire regolarmente in immobili o azioni e ridurre le spese. La strategia IF include una pianificazione a lungo termine, il raggiungimento di obiettivi di reddito e la libertà finanziaria senza dipendere da uno stipendio mensile. Per molti, questo significa avere un portafoglio di investimenti pari almeno a 25 volte i loro costi annuali di vita, con un rendimento del 4% all'anno.",
            "chart": chart_growth("Crescita del portafoglio verso l'IF (CHF)", {
                "Risparmio": [100, 120, 145, 180, 220],
                "Investimento": [100, 130, 180, 250, 330]
            }),
            "link": "https://www.finanztipp.ch/it/indipendenza-finanziaria/"
        },
        {
            "title": "Carta di credito vs. carta di debito: quale è la migliore?",
            "summary": "In Svizzera esistono diversi metodi di pagamento, ma le carte di credito e di debito sono i più comuni. Le carte di credito offrono maggiore flessibilità e premi, ma con costi e tassi d'interesse più elevati. Le carte di debito, invece, addebitano direttamente il tuo conto bancario e generalmente comportano costi inferiori. La scelta tra una carta di credito e di debito dipende dalle tue abitudini di spesa: le carte di credito possono essere vantaggiose per chi ha spese regolari, mentre le carte di debito sono più adatte a chi preferisce spendere solo ciò che ha già.",
            "chart": chart_growth("Premi vs. Costi delle carte di credito", {
                "Premi": [0, 50, 120, 200, 300],
                "Costi": [10, 25, 40, 60, 80]
            }),
            "link": "https://www.finanztipp.ch/it/carte-di-credito-vs-debito/"
        },
        {
            "title": "Scegliere l'assicurazione giusta per le tue esigenze",
            "summary": "Le assicurazioni sono un elemento fondamentale della protezione finanziaria in Svizzera. Esistono vari tipi di assicurazione, come le assicurazioni sulla vita, l'assicurazione sanitaria, la responsabilità civile e la proprietà. La scelta dell'assicurazione dipende dalla tua situazione personale, dalla tua famiglia e dal tuo lavoro. I giovani spesso hanno bisogno solo dell'assicurazione sanitaria e della responsabilità civile, mentre le famiglie potrebbero aver bisogno di assicurazioni sulla vita e sulla proprietà. È importante rivedere regolarmente le proprie assicurazioni e adattarle se necessario.",
            "chart": chart_growth("Tipi di assicurazione più popolari per fascia di età", {
                "Assicurazione sanitaria": [90, 90, 85, 80, 75],
                "Assicurazione sulla vita": [30, 40, 50, 60, 70],
                "Assicurazione sulla proprietà": [20, 30, 40, 50, 60]
            }),
            "link": "https://www.ch.ch/it/assicurazioni/"
        },
        {
            "title": "Pianificare il budget e gestire i debiti in Svizzera",
            "summary": "Il budget è una delle competenze più importanti da acquisire per avere successo finanziariamente in Svizzera. Se vivi in Svizzera, potresti dover affrontare un costo della vita elevato, soprattutto nelle aree urbane. È quindi fondamentale tenere sotto controllo le tue spese e evitare di accumulare debiti. Un buon piano di budget e gestione dei debiti ti aiuterà a gestire le spese impreviste e a risparmiare a lungo termine. Utilizza strumenti di pianificazione del budget online e app per tenere sotto controllo le tue finanze.",
            "chart": chart_growth("Budget vs. Debiti", {
                "Budget": [100, 200, 300, 400, 500],
                "Debiti": [0, 50, 100, 150, 200]
            }),
            "link": "https://www.finanztipp.ch/it/pianificazione-del-budget-e-gestione-dei-debiti/"
        },
        {
            "title": "Come acquistare un immobile in Svizzera",
            "summary": "Acquistare una proprietà in Svizzera è un processo complesso ma gratificante. Devi prima capire le tue opzioni di finanziamento: la maggior parte delle persone in Svizzera ha bisogno di un mutuo per finanziare l'acquisto. Il processo di acquisto include la ricerca della proprietà ideale, la negoziazione, la verifica della due diligence e l'esame dei contratti. Un elemento chiave è comprendere come funzionano le imposte immobiliari e come puoi beneficiare del tuo investimento a lungo termine.",
            "chart": chart_growth("Prezzi delle proprietà in Svizzera (per anno)", {
                "Zurigo": [5000, 5100, 5200, 5300, 5400],
                "Ginevra": [4500, 4600, 4700, 4800, 4900]
            }),
            "link": "https://www.finanztipp.ch/it/acquistare-immobile-in-svizzera/"
        }
    ]
    
    topics_cat = [
        {
            "title": "Pilar 3a Suís Explicat (Säule 3a)",
            "summary": "El Pilar 3a suís, o Säule 3a, és un pla de pensions voluntari que permet als residents suïssos contribuir anualment i deduir-ho dels seus ingressos imposables. Això resulta en estalvis fiscals immediats. Hi ha dos tipus principals de comptes 3a: els oferts per bancs i els oferits per companyies d'assegurances. Els comptes 3a basats en bancs ofereixen més flexibilitat, permetent retirades sota certes condicions com la compra de casa o deixar Suïssa. Les opcions basades en assegurances sovint inclouen assegurança de vida però poden lligar-te a primes fixes. A partir de 2024, es poden contribuir fins a CHF 7.056 anuals (per a treballadors assalariats). Les inversions en comptes 3a poden créixer amb diferiment fiscal, convertint-los en un component essencial de la planificació de la jubilació a Suïssa.",
            "chart": chart_growth("Creciment del Bank vs. Assegurança 3a", {
                "Bank": [100, 112, 126, 140, 155],
                "Insurance": [100, 108, 116, 124, 132]
            }),
            "link": "https://www.ch.ch/en/retirement/third-pillar/"
        },
        {
            "title": "Com Funciona Realment la Krankenkasse",
            "summary": "El sistema d'assegurança de salut de Suïssa, conegut com a Krankenkasse, requereix que tothom tingui una cobertura bàsica (LaMal). Es poden escollir diversos models com Telmed, HMO o el model estàndard. Cada model afecta la teva prima i flexibilitat. L'assegurança suplementària (Zusatzversicherung) ofereix cobertura per habitacions privades d'hospitals o medicina alternativa. Escollint una franquícia més alta, optant per Telmed o HMO i comparant anualment, es poden estalviar més de CHF 1.000/any. Les primes varien segons el cantó, l'edat i el proveïdor. Cada novembre, pots canviar de proveïdor sense penalització, oferint-te una oportunitat clau per optimitzar els teus costos.",
            "chart": chart_growth("Prima Anual per Tipus de Model", {
                "Standard": [4000, 4050, 4100, 4200, 4300],
                "Telmed": [3600, 3620, 3650, 3675, 3700],
                "HMO": [3500, 3525, 3550, 3575, 3600]
            }),
            "link": "https://www.ch.ch/en/health/health-insurance/"
        },
        {
            "title": "Inversions a Suïssa 101",
            "summary": "Començar a invertir a Suïssa és més fàcil del que molts pensen. Pots començar amb tan sols CHF 100/mes utilitzant un corretatge suís. La forma més comuna i amigable per als principiants d'invertir és a través d'ETFs (Fons Cotitzats en Borsa), que proporcionen una exposició diversificada al mercat. Comparat amb els comptes d'estalvi que ofereixen un interès mínim, els ETFs ofereixen rendiments més alts a llarg termini—tot i que amb més risc. Plataformes d'inversió com Swissquote, TrueWealth o VIAC estan dissenyades per a residents. Amb el temps, invertir de manera constant pot superar la inflació i els rendiments dels comptes d'estalvi.",
            "chart": chart_growth("Creciment ETF vs. Estalvi", {
                "ETF": [100, 115, 135, 160, 190],
                "Savings": [100, 101, 102, 104, 106]
            }),
            "link": "https://www.finanztipp.ch/etf/"
        },
        {
            "title": "Deduccions Fiscals que Probablement Estàs Perdent",
            "summary": "Molts residents suïssos perden deduccions fiscals a les quals tenen dret. Les més comunes inclouen les contribucions al Pilar 3a, els costos de desplaçament, les despeses per treballar des de casa, la cura infantil, l'educació continuada i fins i tot les donacions. Depenent del teu cantó, les estratègies per estalviar impostos varien—Zuric, per exemple, permet deduccions generoses per despeses de viatge. Per als autònoms, les deduccions addicionals inclouen equipament d'oficina i primes d'assegurança. Utilitza calculadores en línia o consulta guies fiscals locals per identificar què pots reclamar. Presentar els impostos de manera eficient pot significar estalviar centenars o fins i tot milers de francs anuals.",
            "chart": chart_growth("Estalvi Estimat per Tipus de Deducció (CHF)", {
                "Commuting": [0, 400, 400, 400, 400],
                "3a": [0, 1411, 1411, 1411, 1411],
                "Childcare": [0, 1200, 1200, 1200, 1200]
            }),
            "link": "https://www.ch.ch/en/taxes/deductions/"
        },
        {
            "title": "Pressupost Mensual a Suïssa",
            "summary": "Un pressupost típic a Suïssa segueix la regla 50/30/20: 50% per a necessitats (lloguer, menjar, assegurança), 30% per a desitjos (viatges, lleure) i 20% per a estalvis o pagament de deutes. Aquest model s'ha d'adaptar als alts costos suïssos. Per exemple, el lloguer a Zuric pot ocupar fins al 40% del teu salari. Aplicacions de pressupost com YNAB, Revolut o aplicacions específiques de Suïssa com FinanceFox ajuden a fer un seguiment de les despeses. Crear categories i utilitzar l'automatització (ordres permanents) millora la disciplina a llarg termini.",
            "chart": chart_growth("Assignació del Pressupost Mensual (CHF 5.000)", {
                "Needs": [2500, 2500, 2500, 2500, 2500],
                "Wants": [1500, 1500, 1500, 1500, 1500],
                "Savings": [1000, 1000, 1000, 1000, 1000]
            }),
            "link": "https://www.ch.ch/en/money-budget/"
        },
        {
            "title": "El Veritable Cost de Viure Sol a Suïssa",
            "summary": "Viure sol a Suïssa és un luxe que requereix una planificació acurada. Els costos mensuals típics inclouen CHF 1.500–2.500 per al lloguer (segons la ciutat), CHF 350 per a l'assegurança de salut, CHF 100 per al transport públic, CHF 400–600 per al menjar i CHF 50–100 per a subscripcions. El cost mensual total sovint supera els CHF 3.000. Fer un pressupost i avaluar els ingressos de manera realista és clau abans de decidir viure sol.",
            "chart": chart_growth("Desglossament dels Costos Mensuals de Viure", {
                "Rent": [1800, 1800, 1850, 1900, 1950],
                "Health Insurance": [350, 355, 360, 370, 375],
                "Transport": [100, 105, 105, 110, 110]
            }),
            "link": "https://www.ch.ch/en/living/"
        },
        {
            "title": "Termini de Canvi de la Krankenkasse: Què Necessites Saber",
            "summary": "Els contractes d'assegurança de salut a Suïssa es poden canviar anualment enviant una notificació abans de finals de novembre. Aquesta finestra et permet comparar i canviar a proveïdors més econòmics. Utilitza eines oficials com Priminfo o Comparis per comparar primes. El canvi requereix una Kündigung escrita (carta de terminació) i, de vegades, prova de nova cobertura. No complir amb aquest termini pot costar-te centenars de francs en primes de més.",
            "chart": chart_growth("Diferència de Prima per Proveïdor", {
                "Provider A": [400, 410, 420, 430, 440],
                "Provider B": [380, 385, 390, 395, 400]
            }),
            "link": "https://www.ch.ch/en/health/health-insurance/change-insurance/"
        },
        {
            "title": "Pilar 3a: Banc o Assegurança?",
            "summary": "Escollir entre comptes 3a basats en banc o en assegurança depèn de la flexibilitat i els rendiments. Els bancs permeten més llibertat amb les retirades i millors opcions d'inversió com carteres d'ETF. Les assegurances ofereixen cobertura de vida combinada però t'hi llancen. Durant 20 anys, els bancs sovint ofereixen millors rendiments si es gestionen correctament. Compara les tarifes, els perfils de risc i les condicions de sortida abans de comprometre't.",
            "chart": chart_growth("Comparació del Rendiment a 20 Any", {
                "Bank ETF": [100, 115, 135, 155, 180],
                "Insurance Policy": [100, 108, 116, 124, 132]
            }),
            "link": "https://www.moneyland.ch/en/3a-pillar-bank-or-insurance"
        },
        {
            "title": "Estabilitat del Franc Suís & Inversions",
            "summary": "El Franc Suís (CHF) és conegut mundialment com una moneda 'refugi segur'. Manté el seu valor durant les crisis globals, recolzat per la baixa inflació del Banc Nacional Suís i una política monetària estricta. Els inversors que mantenen actius en CHF redueixen l'exposició a la volatilitat de les monedes. Això fa que Suïssa sigui una base atractiva per a la moneda per a inversors internacionals i conservadors.",
            "chart": chart_growth("Índex d'Estabilitat CHF vs. USD & EUR", {
                "CHF": [100, 102, 103, 104, 106],
                "USD": [100, 98, 96, 95, 97],
                "EUR": [100, 99, 98, 97, 98]
            }),
            "link": "https://www.snb.ch/en/"
        },
        {
            "title": "Expats: Com Navegar per les Finances Suïsses",
            "summary": "Mudar-se a Suïssa comporta una gran corba d'aprenentatge financer. Has de contractar una assegurança de salut obligatòria dins dels primers 3 mesos. Entendre la pensió (AHV, 2n pilar), la presentació d'impostos per cantó i obrir un banc local també són essencials. Comença amb una Krankenkasse bàsica, registra't a la Gemeinde i utilitza aplicacions com TaxInfo o moneyland.ch per estimar les teves finances. Les barreres idiomàtiques poden fer més difícil navegar pel sistema, però una informació estructurada pot estalviar-te temps i diners.",
            "chart": chart_growth("Passos per a la Configuració Financera per a Nous Residents", {
                "Health Insurance": [1, 2, 2, 2, 2],
                "Bank Setup": [1, 1, 2, 2, 2],
                "Tax Registration": [0, 1, 2, 2, 2]
            }),
            "link": "https://www.ch.ch/en/moving-to-switzerland/"
        }
    ]
    
    if language == 'English':
      topics = topics_en
    elif language == 'Deutsch':
      topics = topics_de
    elif language == 'Español':
      topics = topics_es
    elif language == 'Français':
      topics = topics_fr
    elif language == 'Italiano':
      topics = topics_it
    elif language == 'Català':
      topics = topics_cat
    else:
      topics = topics_en

    for topic in topics:
      with st.expander(topic["title"]):
        st.write(topic["summary"])
        st.altair_chart(topic["chart"], use_container_width=True)
        st.markdown(f"🔗 [Official Link]({topic['link']})")
