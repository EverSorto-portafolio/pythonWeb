'use client';
import { useEffect, useState } from "react";
import Layout from "./components/Layout";



interface Article{
  id: number;
  title: string;
  content: string;
}

export default function Home() {
  const [article, setArticle] = useState<Article[]>([]);
  useEffect(() => {
    fetch("http://127.0.0.1:5000/articles")
    .then(response => response.json())
    .then(data => setArticle(data))
    .catch(error => console.error("Error fetching articles:", error));
  }, []);
console.log(article);

  return (
    <Layout>
      <div className="container mx-auto py-10">
        <h1 className="text-4xl font-bold md-6 text-indigo-600">Hola mundo</h1>

      </div>
    </Layout>
  );
}
