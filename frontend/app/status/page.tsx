"use client";

import useSWR from "swr";
import { api } from "@/lib/api";

const fetcher = (url: string) => api.get(url).then(res => res.data);

export default function StatusPage() {
    const { data, isLoading } = useSWR("/status", fetcher, {
        refreshInterval: 5000, // هر 5 ثانیه آپدیت 
    })

    if (isLoading) return <p>... در حال بارگذاری </p>

    return (
        <div className="p-6 space-y-6">
            <h1 className="text-3xl font-bold">وضعیت هم گام سازی</h1>

            <div className="grid grid-cols-4 gap-4">
                <Card title="فایل های جدید" value={data.new_files.length} color="green" />
                <Card title="فایل‌های تغییر یافته" value={data.new_files.length} color="yellow" />
                <Card title="فایل‌های حذف‌شده" value={data.new_files.length} color="red" />
                <Card title="بدون تغییر" value={data.new_files.length} color="blue" />
            </div>

            <FileTable diff={data} />

        </div>
    )

}


function Card({ title, value, color }: any) {
    return (
        <div className={`p-4 rounded-lg bg-${color}-100 border border-${color}-300`}>
            <p className="font-medium">{title}</p>
            <p className="text-2xl font-bold">{value}</p>
        </div>
    )
}

function FileTable({ diff }: any) {
    return (
        <div className="mt-6">
            <h2 className="text-xl mb-2">جزئیات تغییرات</h2>

            <table className="w-full border">
                <thead>
                    <tr className="bg-gray-100">
                        <th className="border p-2">نوع</th>
                        <th className="border p-2">مسیر فایل</th>
                    </tr>
                </thead>

                <tbody>
                    {diff.new_files.map((f: any) => (
                        <Row key={f} type="🆕 جدید" color="green" file={f.path} />
                    ))}

                    {diff.modified_files.map((f: any) => (
                        <Row key={f} type="✏️ تغییر کرده" color="yellow" file={f.path} />
                    ))}

                    {diff.deleted_files.map((f: any) => (
                        <Row key={f} type="🗑️ حذف شده" color="red" file={f} />
                    ))}

                    {diff.unchanged_files.map((f: any) => (
                        <Row key={f} type="✔ بدون تغییر" color="green" file={f.path} />
                    ))}
                </tbody>
            </table>
        </div>
    )
}

function Row({ type, file, color }: any) {
    return (
        <tr className={`border-l-4 border-${color}-500`}>
            <td className="border p-2">{type}</td>
            <td className="border p-2">{file}</td>
        </tr>
    )
}