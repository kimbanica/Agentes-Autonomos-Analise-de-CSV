window.onload = function () {
  const perguntas = [
    "Qual é o fornecedor que teve maior montante recebido?",
    "Qual o valor total das notas fiscais emitidas?",
    "Quantas notas foram emitidas no mês?",
    "Qual o município do fornecedor mais recorrente?",
    "Qual foi o produto mais vendido?"
  ];

  const textarea = document.querySelector("textarea");
  const form = textarea?.closest("form");

  if (form && textarea) {
    const container = document.createElement("div");
    container.style.margin = "10px 0";

    perguntas.forEach((texto) => {
      const btn = document.createElement("button");
      btn.innerText = texto;
      btn.style.margin = "4px";
      btn.style.backgroundColor = "#d4af37";
      btn.style.color = "#000";
      btn.style.border = "1px solid #bfa334";
      btn.style.borderRadius = "4px";
      btn.style.padding = "6px 10px";
      btn.onclick = (e) => {
        e.preventDefault();
        textarea.value = texto;
      };
      container.appendChild(btn);
    });

    form.insertBefore(container, textarea);
    textarea.placeholder = "Digite sua pergunta sobre os dados das notas fiscais...";
  }
};
